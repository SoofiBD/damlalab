from django.contrib import admin
from .models import research_topic, member, Project, Thesis , Researcher , Scholar, Coordinator, Announcement, Slideshow

@admin.register(Scholar)
class ScholarAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'affiliation', 'date')
    search_fields = ('name', 'affiliation')
    ordering = ('-date',)

@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'affiliation', 'date')
    search_fields = ('name', 'affiliation')
    ordering = ('-date',)

@admin.register(Researcher)
class ResearcherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'affiliation', 'date')
    search_fields = ('name', 'affiliation')
    ordering = ('-date',)
    
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
    
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'content')
    ordering = ('-date',)

@admin.register(Slideshow)
class SlideshowAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)

