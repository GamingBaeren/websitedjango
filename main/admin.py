from django.contrib import admin
from django import forms
from .models import SiteSettings

class SiteSettingsAdminForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = '__all__'
        widgets = {
            'light_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'light_text_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_text_color': forms.TextInput(attrs={'type': 'color'}),
            'light_navbar_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'light_navbar_text_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_navbar_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_navbar_text_color': forms.TextInput(attrs={'type': 'color'}),
            'light_footer_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'light_footer_text_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_footer_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_footer_text_color': forms.TextInput(attrs={'type': 'color'}),
        }

class SiteSettingsAdmin(admin.ModelAdmin):
    form = SiteSettingsAdminForm

    def has_add_permission(self, request):
        # Allow adding only if no SiteSettings instance exists
        if SiteSettings.objects.exists():
            return False
        return True

admin.site.register(SiteSettings, SiteSettingsAdmin)
