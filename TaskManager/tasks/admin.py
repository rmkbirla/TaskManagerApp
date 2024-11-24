from django.contrib import admin
from .models import Task, OAuthKeys

admin.site.register(Task)
admin.site.register(OAuthKeys)
