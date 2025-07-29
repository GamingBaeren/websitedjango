from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.urls import reverse_lazy
from .forms import UserUpdateForm, CustomPasswordChangeForm, CustomUserCreationForm, CustomPasswordResetForm
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from .utils import send_test_email

def test_email(request):
    try:
        send_test_email()
        return HttpResponse("Test email sent successfully.")
    except Exception as e:
        return HttpResponse(f"Failed to send test email: {e}")


def home(request):
    return render(request, 'main/home.html')

def impressum(request):
    return render(request, 'main/impressum.html')

def contact(request):
    return render(request, 'main/contact.html')

@login_required
def profile(request):
    return render(request, 'main/profile.html')

@login_required
def settings(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'main/settings.html', {'form': form})

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')

from .forms import CustomAuthenticationForm

class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    authentication_form = CustomAuthenticationForm

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'main/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        return render(request, 'main/register.html', {'form': form})

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

@login_required
def test_password_change(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('password_change_done')
    return render(request, 'registration/password_change_form.html', {'form': form})
