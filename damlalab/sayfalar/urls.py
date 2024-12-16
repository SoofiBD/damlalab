from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('research/', views.research, name='research'),
    path('research_group/', views.research_group, name='research_group'),
    path('positions/', views.positions, name='positions'),
    path('thesis/', views.thesis, name='thesis'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]