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
            'blog_heading_text': forms.TextInput(attrs={'type': 'text'}),
            'light_blog_heading_text_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_blog_heading_text_color': forms.TextInput(attrs={'type': 'color'}),
            'light_navbar_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'light_navbar_text_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_navbar_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_navbar_text_color': forms.TextInput(attrs={'type': 'color'}),
            'light_footer_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'light_footer_text_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_footer_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_footer_text_color': forms.TextInput(attrs={'type': 'color'}),
            'light_intermediate_heading_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_intermediate_heading_color': forms.TextInput(attrs={'type': 'color'}),
            'light_container_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_container_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'light_imageupload_container_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_imageupload_container_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'light_imageupload_text_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_imageupload_text_color': forms.TextInput(attrs={'type': 'color'}),
            'light_socialmedia_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_socialmedia_bg_color': forms.TextInput(attrs={'type': 'color'}),
            'light_socialmedia_text_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_socialmedia_text_color': forms.TextInput(attrs={'type': 'color'}),
            'light_socialmedia_links_text_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_socialmedia_links_text_color': forms.TextInput(attrs={'type': 'color'}),
            'light_socialmedia_heading_text_color': forms.TextInput(attrs={'type': 'color'}),
            'dark_socialmedia_heading_text_color': forms.TextInput(attrs={'type': 'color'}),
        }

class SiteSettingsAdmin(admin.ModelAdmin):
    form = SiteSettingsAdminForm

    def has_add_permission(self, request):
        # Allow adding only if no SiteSettings instance exists
        if SiteSettings.objects.exists():
            return False
        return True

admin.site.register(SiteSettings, SiteSettingsAdmin)
