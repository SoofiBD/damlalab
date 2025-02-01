from django.shortcuts import render
from .models import member, Project, Thesis, research_topic, Announcement

def home(request):
    topics = research_topic.objects.all().order_by('-date')[:6]  
    announcements = Announcement.objects.all().order_by('-date') 
    context = {
        'topics': topics,
        'announcements': announcements,
    }
    return render(request, 'index.html', context)

def research(request):
    topics = research_topic.objects.all().order_by('-date')
    context = {
        'topics': topics,
    }
    return render(request, 'topics.html', context)

def members(request):
    group_leaders = member.objects.filter(title='GL').order_by('-date')
    graduate_students = member.objects.filter(title='GS').order_by('-date')
    previous_members = member.objects.filter(title='PM').order_by('-date')
    context = {
        'group_leaders': group_leaders,
        'graduate_students': graduate_students,
        'previous_members': previous_members,
    }
    return render(request, 'members.html', context)

def projects(request):
    research_projects = Project.objects.filter(project_type='research').order_by('-date')
    student_projects = Project.objects.filter(project_type='student').order_by('-date')
    context = {
        'research_projects': research_projects,
        'student_projects': student_projects,
    }
    return render(request, 'projects.html', context)

def positions(request):
    return render(request, 'positions.html')

def theses(request):
    ongoing_theses = Thesis.objects.filter(status='ongoing').order_by('-date_created')
    completed_theses = Thesis.objects.filter(status='completed').order_by('-date_created')
    context = {
        'ongoing_theses': ongoing_theses,
        'completed_theses': completed_theses,
    }
    return render(request, 'theses.html', context)

def contact(request):
    return render(request, 'contact.html')
