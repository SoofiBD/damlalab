from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def research(request):
    return render(request, 'research.html')

def research_group(request):
    return render(request, 'researchgroup.html')

def positions(request):
    return render(request, 'positions.html')

def thesis(request):
    return render(request, 'theses.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')
