from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def research(request):
    return render(request, 'topics.html')

def members(request):
    return render(request, 'members.html')  

def projects(request):
    return render(request, 'projects.html')

def positions(request):
    return render(request, 'positions.html')

def theses(request):
    return render(request, 'theses.html')

def contact(request):
    return render(request, 'contact.html')