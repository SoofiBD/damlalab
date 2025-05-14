from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from .models import (
    Announcement,
    Thesis, ThesisParticipation,
    Project, ProjectParticipation,
    Person , Position
)

def home(request):
    announcements = Announcement.objects.filter(is_published=True).order_by('-date')
    return render(request, 'index.html', {
        'announcements': announcements,
    })

def theses(request):
    ongoing   = Thesis.objects.filter(is_published=True, status=Thesis.STATUS_ONGOING) \
                              .order_by('-start_date')
    completed = Thesis.objects.filter(is_published=True, status=Thesis.STATUS_COMPLETE) \
                              .order_by('-end_date')

    for qs in (ongoing, completed):
        for thesis in qs:
            parts = thesis.thesisparticipation_set.select_related('person').all()
            thesis.students    = [p.person.name for p in parts if p.role == Person.ROLE_STUDENT]
            thesis.supervisors = [p.person.name for p in parts if p.role == Person.ROLE_SUPERVISOR]
            thesis.pis         = [p.person.name for p in parts if p.role == Person.ROLE_PI]
            if not thesis.slug:
                thesis.slug = slugify(thesis.title)

    return render(request, 'theses.html', {
        'ongoing_theses': ongoing,
        'completed_theses': completed,
    })

def thesis_detail(request, slug):
    thesis = get_object_or_404(Thesis, slug=slug, is_published=True)
    parts   = thesis.thesisparticipation_set.select_related('person').all()
    students    = [p.person for p in parts if p.role == Person.ROLE_STUDENT]
    supervisors = [p.person for p in parts if p.role == Person.ROLE_SUPERVISOR]
    pis         = [p.person for p in parts if p.role == Person.ROLE_PI]

    return render(request, 'thesis_detail.html', {
        'thesis': thesis,
        'students': students,
        'supervisors': supervisors,
        'pis': pis,
    })

def projects(request):
    research_projects = Project.objects.filter(
        project_type=Project.PROJECT_TYPE_RESEARCH,
        is_published=True
    ).order_by('-start_date')
    student_projects = Project.objects.filter(
        project_type=Project.PROJECT_TYPE_STUDENT,
        is_published=True
    ).order_by('-start_date')

    return render(request, 'projects.html', {
        'research_projects': research_projects,
        'student_projects': student_projects,
    })

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_published=True)
    parts   = project.projectparticipation_set.select_related('person').all()
    students    = [p.person for p in parts if p.role == Person.ROLE_STUDENT]
    supervisors = [p.person for p in parts if p.role == Person.ROLE_SUPERVISOR]
    pis         = [p.person for p in parts if p.role == Person.ROLE_PI]

    return render(request, 'projects_detail.html', {
        'project': project,
        'students': students,
        'supervisors': supervisors,
        'pis': pis,
    })
    
def members(request):
    thesis_parts   = ThesisParticipation.objects.select_related('person')
    project_parts  = ProjectParticipation.objects.select_related('person')

    students    = {p.person for p in thesis_parts if p.role == Person.ROLE_STUDENT}
    students   |= {p.person for p in project_parts if p.role == Person.ROLE_STUDENT}

    supervisors = {p.person for p in thesis_parts if p.role == Person.ROLE_SUPERVISOR}
    supervisors |= {p.person for p in project_parts if p.role == Person.ROLE_SUPERVISOR}

    pis         = {p.person for p in thesis_parts if p.role == Person.ROLE_PI}
    pis        |= {p.person for p in project_parts if p.role == Person.ROLE_PI}

    context = {
        'students':    list(students),
        'supervisors': list(supervisors),
        'pis':         list(pis),
    }
    return render(request, 'members.html', context)

def contact(request):
    return render(request, 'contact.html')

def positions(request):
    positions = Position.objects.filter(is_published=True).order_by('order')
    return render(request, 'positions.html', {
        'positions': positions,
    })
