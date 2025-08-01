from django.db import models
from django.core.exceptions import ValidationError

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default='GamingBaeren.de')
    light_bg_color = models.CharField(max_length=7, default='#f5f0e9', help_text='Hex color for light mode background')
    light_text_color = models.CharField(max_length=7, default='#000000', help_text='Hex color for light mode text')
    dark_bg_color = models.CharField(max_length=7, default='#000000', help_text='Hex color for dark mode background')
    dark_text_color = models.CharField(max_length=7, default='#d1d5db', help_text='Hex color for dark mode text')

    light_navbar_bg_color = models.CharField(max_length=7, default='#1f2937', help_text='Hex color for light mode navbar background')
    light_navbar_text_color = models.CharField(max_length=7, default='#d1d5db', help_text='Hex color for light mode navbar text')
    dark_navbar_bg_color = models.CharField(max_length=7, default='#111827', help_text='Hex color for dark mode navbar background')
    dark_navbar_text_color = models.CharField(max_length=7, default='#f9fafb', help_text='Hex color for dark mode navbar text')

    light_footer_bg_color = models.CharField(max_length=7, default='#f9fafb', help_text='Hex color for light mode footer background')
    light_footer_text_color = models.CharField(max_length=7, default='#1f2937', help_text='Hex color for light mode footer text')
    dark_footer_bg_color = models.CharField(max_length=7, default='#111827', help_text='Hex color for dark mode footer background')
    dark_footer_text_color = models.CharField(max_length=7, default='#f9fafb', help_text='Hex color for dark mode footer text')

    def clean(self):
        if SiteSettings.objects.exists() and not self.pk:
            raise ValidationError('Only one SiteSettings instance is allowed.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"
