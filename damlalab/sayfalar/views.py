from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.db.models import Q
from .models import (
    Announcement,
    Thesis,
    Project,
    Person,
    Position,
)

def home(request):
    announcements = Announcement.objects.filter(is_published=True).order_by('-date')
    return render(request, 'index.html', {
        'announcements': announcements,
    })

def theses(request):
    ongoing = Thesis.objects.filter(
        is_published=True, status=Thesis.STATUS_ONGOING
    ).order_by('-start_date').prefetch_related('thesisparticipation_set__person')

    completed = Thesis.objects.filter(
        is_published=True, status=Thesis.STATUS_COMPLETE
    ).order_by('-end_date').prefetch_related('thesisparticipation_set__person')

    for qs in (ongoing, completed):
        for thesis in qs:
            parts = thesis.thesisparticipation_set.all()
            thesis.students = [p.person.name for p in parts if p.role == Person.ROLE_STUDENT]
            thesis.supervisors = [p.person.name for p in parts if p.role == Person.ROLE_SUPERVISOR]
            thesis.pis = [p.person.name for p in parts if p.role == Person.ROLE_PI]
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
    ).order_by('-start_date').prefetch_related('projectparticipation_set__person')

    student_projects = Project.objects.filter(
        project_type=Project.PROJECT_TYPE_STUDENT,
        is_published=True
    ).order_by('-start_date').prefetch_related('projectparticipation_set__person')

    return render(request, 'projects.html', {
        'research_projects': research_projects,
        'student_projects': student_projects,
    })

def project_detail(request, slug):
    project = get_object_or_404(Project.objects.prefetch_related('projectparticipation_set__person'), slug=slug, is_published=True)
    parts = project.projectparticipation_set.all()
    students = [p.person for p in parts if p.role == Person.ROLE_STUDENT]
    supervisors = [p.person for p in parts if p.role == Person.ROLE_SUPERVISOR]
    pis = [p.person for p in parts if p.role == Person.ROLE_PI]

    return render(request, 'projects_detail.html', {
        'project': project,
        'students': students,
        'supervisors': supervisors,
        'pis': pis,
    })
    
def members(request):
    students = Person.objects.filter(
        Q(thesisparticipation__role=Person.ROLE_STUDENT) | Q(projectparticipation__role=Person.ROLE_STUDENT)
    ).distinct()

    supervisors = Person.objects.filter(
        Q(thesisparticipation__role=Person.ROLE_SUPERVISOR) | Q(projectparticipation__role=Person.ROLE_SUPERVISOR)
    ).distinct()

    pis = Person.objects.filter(
        Q(thesisparticipation__role=Person.ROLE_PI) | Q(projectparticipation__role=Person.ROLE_PI)
    ).distinct()

    context = {
        'students': list(students),
        'supervisors': list(supervisors),
        'pis': list(pis),
    }
    return render(request, 'members.html', context)

def contact(request):
    return render(request, 'contact.html')

def positions(request):
    positions = Position.objects.filter(is_published=True).order_by('order')
    return render(request, 'positions.html', {
        'positions': positions,
    })
