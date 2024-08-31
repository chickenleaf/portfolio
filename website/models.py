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
