from django.db import models

class research_topic(models.Model):
    topic = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/' , blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.topic
    
class member(models.Model):
    TITLE_CHOICES = [
        ('GL', 'Group Leader'),
        ('GS', 'Graduate Student'),
        ('PM', 'Previous Member'),
    ]
    
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, choices=TITLE_CHOICES)
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    PROJECT_TYPE_CHOICES = (
        ('research', 'Research Projects'),
        ('student', 'Student Projects'),
    )
    
    title = models.CharField(max_length=100)
    project_type = models.CharField(
        max_length=10,
        choices=PROJECT_TYPE_CHOICES,
        default='research',
        help_text="Select whether this is a Research Project or a Student Project."
    )
    start_date = models.DateField()
    end_date = models.DateField()
    researchers = models.ManyToManyField(member, related_name='research_projects', blank=True)
    coordinators = models.ManyToManyField(member, related_name='coordinated_projects', blank=True)
    scholars = models.ManyToManyField(member, related_name='scholar_projects', blank=True)
    description = models.TextField()
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Thesis(models.Model):
    THESIS_STATUS_CHOICES = (
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    )
    
    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=10,
        choices=THESIS_STATUS_CHOICES,
        default='ongoing',
        help_text="Select whether the thesis is ongoing or completed."
    )
    author = models.CharField(max_length=100, help_text="Name of the thesis author.")
    start_date = models.DateField(help_text="The start date of the thesis.")
    end_date = models.DateField(null=True, blank=True, help_text="The end date of the thesis (if applicable).")
    description = models.TextField(blank=True, help_text="Optional additional details about the thesis.")
    date_created = models.DateTimeField(auto_now_add=True)
    link = models.URLField(blank=True, help_text="Link to the thesis (if available).")
    
    def __str__(self):
        return self.title
    