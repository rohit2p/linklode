from django.db import models


class JobCategory(models.TextChoices):
    GOVERNMENT = 'government', 'Government'
    PRIVATE = 'private', 'Private'
    INTERNSHIP = 'internship', 'Internship'


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=150, blank=True)
    category = models.CharField(max_length=20, choices=JobCategory.choices, default=JobCategory.PRIVATE)
    description = models.TextField()
    location = models.CharField(max_length=100, blank=True)
    deadline = models.DateField()
    apply_link = models.URLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ResourceCategory(models.TextChoices):
    NOTES = 'notes', 'Notes'
    PREVIOUS_PAPERS = 'previous_papers', 'Previous Year Papers'
    SYLLABUS = 'syllabus', 'Syllabus'
    BOOKS = 'books', 'Books'
    OTHER = 'other', 'Other'


class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=30, choices=ResourceCategory.choices, default=ResourceCategory.NOTES)
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    external_link = models.URLField(blank=True)  # for Google Drive, etc.
    thumbnail = models.ImageField(upload_to='resource_thumbs/', blank=True, null=True)
    download_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_download_url(self):
        if self.file:
            return self.file.url
        return self.external_link


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"