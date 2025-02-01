from django.contrib import admin
from .models import research_topic, member, Project, Thesis

@admin.register(research_topic)
class ResearchTopicAdmin(admin.ModelAdmin):
    list_display = ('topic', 'date')
    search_fields = ('topic', 'description')
    ordering = ('-date',)
    
@admin.register(member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'date')
    search_fields = ('name',)
    list_filter = ('title',)
    ordering = ('-date',)
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'start_date', 'end_date', 'date')
    search_fields = ('title', 'description')
    list_filter = ('project_type', 'start_date', 'end_date')
    ordering = ('-date',)
    filter_horizontal = ('researchers', 'coordinators', 'scholars') 

@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'start_date', 'end_date', 'date_created')
    search_fields = ('title', 'author', 'description')
    list_filter = ('status', 'start_date', 'end_date')
    ordering = ('-date_created',)
