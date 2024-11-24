
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class OAuthKeys(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
