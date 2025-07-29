from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
            }),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Altes Passwort",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'autofocus': True,
            'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
        }),
    )
    new_password1 = forms.CharField(
        label="Neues Passwort",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
        }),
    )
    new_password2 = forms.CharField(
        label="Neues Passwort bestätigen",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
        }),
    )

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django import forms

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
        })
    )
    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Override send_mail to customize the email content.
        """
        from django.core.mail import EmailMultiAlternatives
        from django.template.loader import render_to_string

        subject = render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())

        body = render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name:
            html_email = render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="Neues Passwort",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
        }),
    )
    new_password2 = forms.CharField(
        label="Neues Passwort bestätigen",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
        }),
    )

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Passwort",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
        }),
    )
    password2 = forms.CharField(
        label="Passwort wiederholen",
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
        }),
        strip=False,
    )
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
            }),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'rounded-md bg-white text-black px-3 py-2 w-full',
        'autofocus': True,
        'autocomplete': 'username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'rounded-md bg-white text-black px-3 py-2 w-full',
        'autocomplete': 'current-password',
    }))
