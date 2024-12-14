from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def research(request):
    return render(request, 'research.html')
