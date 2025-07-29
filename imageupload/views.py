from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, LoginView
from django.urls import reverse_lazy
from main.forms import UserUpdateForm, CustomPasswordChangeForm, CustomUserCreationForm, CustomPasswordResetForm
from .forms import ImageUploadForm
from django.contrib.auth import login
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
# Removed import of send_test_email as utils.py does not exist
from django.utils.timezone import now
from django.contrib.auth.decorators import user_passes_test

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

from main.forms import CustomAuthenticationForm

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

@login_required
def test_password_change(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('password_change_done')
    return render(request, 'registration/password_change_form.html', {'form': form})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploader = request.user
            # For non-admin users, enforce max retention_days 30
            if not request.user.is_staff:
                if image.retention_days is None or image.retention_days > 30:
                    image.retention_days = 30
            else:
                # Admin users can have unlimited retention (None or 0)
                if image.retention_days == 0:
                    image.retention_days = None
            image.save()
            messages.success(request, "Image uploaded successfully.")
            return redirect('imageupload:image_detail', image_id=image.id)
    else:
        form = ImageUploadForm()
    return render(request, 'imageupload/upload_image.html', {'form': form})

def how_it_works(request):
    return render(request, 'imageupload/how_it_works.html')

@login_required
def image_detail(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    file_size = image.get_file_size()
    direct_url = image.image.url
    view_url = request.build_absolute_uri(image.get_absolute_url()) if hasattr(image, 'get_absolute_url') else direct_url
    return render(request, 'imageupload/image_detail.html', {
        'image': image,
        'file_size': file_size,
        'direct_url': direct_url,
        'view_url': view_url,
    })
