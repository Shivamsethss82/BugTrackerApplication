from django.db import models

# Create your models here.
class Myform(models.Model):
    BUG_OS_CHOICES = [
        ('windows', 'Windows'),
        ('mac', 'Mac'),
        ('linux', 'Linux'),
        ('other', 'Other'),
    ]

    bug_title = models.CharField(max_length=100)
    issue_description = models.TextField()
    os = models.CharField(max_length=20, choices=BUG_OS_CHOICES)
    browser = models.CharField(max_length=20)
    assigned_to = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    screenshot = models.ImageField(upload_to='main', blank=True, null=True)
    status = models.CharField(max_length=20)
    
    def __str__(self):
        return self.bug_title