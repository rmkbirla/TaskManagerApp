# admin_panel/forms.py
from django import forms
from tasks.models import OAuthKeys
from .models import UserInvitation

class OAuthKeysForm(forms.ModelForm):
    class Meta:
        model = OAuthKeys
        fields = ['client_id', 'client_secret']

class UserInvitationForm(forms.ModelForm):
    class Meta:
        model = UserInvitation
        fields = ['email']
