from django.contrib import admin
from .models import Person, Announcement, Thesis, ThesisParticipation , Project, ProjectParticipation , Position

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display  = ('name', 'email', 'affiliation')
    search_fields = ('name', 'email')


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display  = ('title', 'date', 'is_published')
    list_filter   = ('is_published', 'date')
    search_fields = ('title',)


class ThesisParticipationInline(admin.TabularInline):
    model               = ThesisParticipation
    extra               = 1
    autocomplete_fields = ['person']


@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display  = ('title', 'status', 'start_date', 'end_date', 'is_published')
    list_filter   = ('status', 'is_published')
    search_fields = ('title', 'abstract')

    inlines = [ThesisParticipationInline]

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'status',
                'start_date', 'end_date',
                'image', 'pdf', 'abstract',
                'link', 'is_published',
            )
        }),
        ('Participants', {
            'classes': ('collapse',),
            'fields': (),
            'description': 'Add Students, Supervisors and Principal Investigator via the inline below.'
        }),
    )
class ProjectParticipationInline(admin.TabularInline):
    model               = ProjectParticipation
    extra               = 1
    autocomplete_fields = ['person']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('title', 'project_type', 'start_date', 'end_date', 'is_published')
    list_filter   = ('project_type', 'is_published')
    search_fields = ('title', 'description')
    inlines       = [ProjectParticipationInline]
    fieldsets     = (
        (None, {
            'fields': (
                'title', 'project_type',
                'start_date', 'end_date',
                'image', 'description',
                'link', 'is_published',
            )
        }),
        ('Participants', {
            'classes': ('collapse',),
            'fields': (),
            'description': 'Add Students, Supervisors and PI via inline.'
        }),
    )
    
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display    = ('title', 'position_type', 'is_published', 'order')
    list_filter     = ('position_type', 'is_published')
    search_fields   = ('title', 'description', 'skills', 'eligibility')
    list_editable  = ('is_published', 'order')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': (
                'title', 'slug', 'position_type', 'is_published', 'order'
            )
        }),
        ('Details', {
            'fields': (
                'description', 'eligibility', 'skills', 'commitment', 'contact_email'
            )
        }),
    )