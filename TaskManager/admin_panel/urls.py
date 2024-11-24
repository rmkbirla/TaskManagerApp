from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='admin_dashboard'),
    path('manage-oauth/', views.manage_oauth_keys, name='manage_oauth'),
    path('invite-user/', views.invite_user, name='invite_user'),
]
