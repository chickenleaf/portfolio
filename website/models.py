from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.subject


class DownloadLog(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    file_name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"Downloaded {self.file_name} on {self.timestamp} from {self.ip_address}"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    major = models.CharField(max_length=200, blank=True, null=True) # For specific majors if needed
    university = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    description = models.TextField(help_text="Use <li> for bullet points. E.g., <li>Subject 1</li><li>Subject 2</li>")
    order = models.IntegerField(unique=True, help_text="Order in which this education should appear")

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} at {self.university}"


class WorkExperience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50, help_text="e.g., Dec 2024")
    end_date = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., Mar 2025 or 'Present'")
    description = models.TextField(help_text="Use <li> for bullet points. E.g., <li>Task 1</li><li>Task 2</li>")
    order = models.IntegerField(unique=True, help_text="Order in which this experience should appear")

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Work Experience"

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, help_text="e.g., App, Data, Web")
    technologies = models.CharField(max_length=200, help_text="Comma-separated technologies, e.g., Python, Transformers API")
    image = models.ImageField(upload_to='project_images/')
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True, help_text="Link to a live demo or more details (if applicable)")
    order = models.IntegerField(unique=True, help_text="Order in which this project should appear")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Achievement(models.Model):
    # This field will hold the full HTML for your points (e.g., <ul><li>...</li></ul>)
    content = models.TextField(
        help_text="Enter your achievement points using full HTML tags (e.g., <ul><li>Point 1</li><li>Point 2</li></ul>)."
    )
    order = models.IntegerField(
        unique=True,
        help_text="Order in which this achievement block should appear (lower numbers first)"
    )

    class Meta:
        ordering = ['order'] # Ensures the section displays in the order you define
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"

    def __str__(self):
        # A simple string representation for the admin list
        # You might want to display the first few words of the content
        return f"Achievement Block {self.order}"
