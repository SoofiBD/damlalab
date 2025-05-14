from django.db import models
from django.utils.text import slugify

class Person(models.Model):
    ROLE_STUDENT    = 'student'
    ROLE_SUPERVISOR = 'supervisor'
    ROLE_PI         = 'principal_investigator'
    ROLE_CHOICES    = [
        (ROLE_STUDENT,    'Student'),
        (ROLE_SUPERVISOR, 'Supervisor'),
        (ROLE_PI,         'Principal Investigator'),
    ]

    name        = models.CharField(max_length=100)
    email       = models.EmailField(blank=True)
    affiliation = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    title        = models.CharField(max_length=200)
    date         = models.DateField(auto_now_add=True)
    short_info   = models.TextField()
    image        = models.ImageField(
        upload_to='announcements/',
        null=True,
        blank=True
    )
    link         = models.URLField(blank=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Thesis(models.Model):
    STATUS_ONGOING  = 'ongoing'
    STATUS_COMPLETE = 'completed'
    STATUS_CHOICES  = [
        (STATUS_ONGOING,  'Ongoing'),
        (STATUS_COMPLETE, 'Completed'),
    ]

    title        = models.CharField(max_length=200)
    slug         = models.SlugField(max_length=220, unique=True, blank=True)
    status       = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_ONGOING
    )
    start_date   = models.DateField()
    end_date     = models.DateField(null=True, blank=True)
    image        = models.ImageField(
        upload_to='theses/',
        null=True,
        blank=True
    )
    abstract     = models.TextField(
        blank=True,
        help_text="A brief summary of the thesis."
    )
    pdf          = models.FileField(
        upload_to='theses/papers/',
        blank=True,
        help_text="Optional PDF of the full thesis."
    )
    link         = models.URLField(blank=True, null=True)
    is_published = models.BooleanField(default=True)

    participants = models.ManyToManyField(
        Person,
        through='ThesisParticipation',
        related_name='theses'
    )

    class Meta:
        ordering = ['-start_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:200]
            slug = base
            num = 1
            while Thesis.objects.filter(slug=slug).exists():
                slug = f"{base}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ThesisParticipation(models.Model):
    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role   = models.CharField(
        max_length=30,
        choices=Person.ROLE_CHOICES
    )

    class Meta:
        unique_together = ('thesis', 'person', 'role')

    def __str__(self):
        role_display = dict(Person.ROLE_CHOICES).get(self.role, self.role)
        return f"{self.person.name} as {role_display} in {self.thesis.title}"

class Project(models.Model):
    PROJECT_TYPE_RESEARCH = 'research'
    PROJECT_TYPE_STUDENT  = 'student'
    PROJECT_TYPE_CHOICES  = [
        (PROJECT_TYPE_RESEARCH, 'Research Project'),
        (PROJECT_TYPE_STUDENT,  'Student Project'),
    ]

    title        = models.CharField(max_length=200)
    slug         = models.SlugField(max_length=220, unique=True, blank=True)
    project_type = models.CharField(
        max_length=10,
        choices=PROJECT_TYPE_CHOICES,
        default=PROJECT_TYPE_RESEARCH
    )
    start_date   = models.DateField()
    end_date     = models.DateField(null=True, blank=True)
    description  = models.TextField(blank=True)
    image        = models.ImageField(
        upload_to='projects/',
        null=True,
        blank=True
    )
    link         = models.URLField(blank=True, null=True)
    is_published = models.BooleanField(default=True)

    participants = models.ManyToManyField(
        Person,
        through='ProjectParticipation',
        related_name='projects'
    )

    class Meta:
        ordering = ['-start_date']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:200]
            slug = base
            num = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectParticipation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    person  = models.ForeignKey(Person,  on_delete=models.CASCADE)
    role    = models.CharField(
        max_length=30,
        choices=Person.ROLE_CHOICES
    )

    class Meta:
        unique_together = ('project', 'person', 'role')

    def __str__(self):
        role_display = dict(Person.ROLE_CHOICES).get(self.role, self.role)
        return f"{self.person.name} as {role_display} in {self.project.title}"
    
class Position(models.Model):
    TYPE_UNDERGRADUATE = 'UG'
    TYPE_GRADUATE      = 'GR'
    TYPE_POSTDOC       = 'PD'
    TYPE_CHOICES       = [
        (TYPE_UNDERGRADUATE, 'Undergraduate'),
        (TYPE_GRADUATE,      'Graduate'),
        (TYPE_POSTDOC,       'Postdoctoral'),
    ]

    title           = models.CharField(max_length=200)
    slug            = models.SlugField(max_length=220, unique=True, blank=True)
    position_type   = models.CharField(
                          max_length=2,
                          choices=TYPE_CHOICES,
                          default=TYPE_UNDERGRADUATE,
                      )
    description     = models.TextField(help_text="Main description of the position")
    eligibility     = models.TextField(blank=True, help_text="Who is eligible")
    skills          = models.TextField(blank=True, help_text="Required skills")
    commitment      = models.CharField(
                          max_length=100,
                          blank=True,
                          help_text="E.g. '10–15 hrs/week' or '2–3 years'"
                      )
    contact_email   = models.EmailField(help_text="Email to apply")
    is_published    = models.BooleanField(default=True)
    order           = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ['order', 'position_type', 'title']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:200]
            slug = base
            cnt = 1
            while Position.objects.filter(slug=slug).exists():
                slug = f"{base}-{cnt}"
                cnt += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_position_type_display()}: {self.title}"