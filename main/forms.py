from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
            }),
            'email': forms.EmailInput(attrs={
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
