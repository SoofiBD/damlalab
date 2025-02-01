from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('topics/', views.research, name='research'),
    path('members/', views.members, name='members'),
    path('projects/', views.projects, name='projects'),
    path('positions/', views.positions, name='positions'),
    path('theses/', views.theses, name='theses'),
    path('contact/', views.contact, name='contact'),
]
