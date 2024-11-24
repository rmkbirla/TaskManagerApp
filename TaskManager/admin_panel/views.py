# admin_panel/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from tasks.models import OAuthKeys
from .models import UserInvitation
from .forms import OAuthKeysForm, UserInvitationForm

# Ensure only admin users can access
def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def dashboard(request):
    return render(request, 'admin_panel/dashboard.html')

@login_required
@user_passes_test(is_admin)
def manage_oauth_keys(request):
    if request.method == 'POST':
        form = OAuthKeysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = OAuthKeysForm()
    keys = OAuthKeys.objects.filter(admin=request.user)
    return render(request, 'admin_panel/manage_oauth_keys.html', {'form': form, 'keys': keys})

@login_required
@user_passes_test(is_admin)
def invite_user(request):
    if request.method == 'POST':
        form = UserInvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save(commit=False)
            invitation.invited_by = request.user
            invitation.save()
            send_mail(
                subject="You’re Invited!",
                message=f"Register using this link: http://127.0.0.1:8000/register/?token={invitation.token}",
                from_email="admin@yourdomain.com",
                recipient_list=[invitation.email]
            )
            return redirect('admin_dashboard')
    else:
        form = UserInvitationForm()
    invitations = UserInvitation.objects.filter(invited_by=request.user)
    return render(request, 'admin_panel/invite_user.html', {'form': form, 'invitations': invitations})
