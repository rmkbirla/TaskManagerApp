# admin_panel/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class UserInvitation(models.Model):
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=50, blank=True, null=True)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    invited_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = get_random_string(length=32)  # Generate a unique token
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invitation to {self.email}"
