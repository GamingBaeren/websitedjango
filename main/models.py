from django.db import models
from django.core.exceptions import ValidationError

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default='GamingBaeren.de')
    light_bg_color = models.CharField(max_length=7, default='#f5f0e9', help_text='Hex color for light mode background')
    light_text_color = models.CharField(max_length=7, default='#000000', help_text='Hex color for light mode text')
    dark_bg_color = models.CharField(max_length=7, default='#000000', help_text='Hex color for dark mode background')
    dark_text_color = models.CharField(max_length=7, default='#d1d5db', help_text='Hex color for dark mode text')

    light_blog_heading_text_color = models.CharField(max_length=7, default='#ffffff', help_text='Hex color for light mode blog heading text')
    dark_blog_heading_text_color = models.CharField(max_length=7, default='#d1d5db', help_text='Hex color for dark mode blog heading text')

    light_navbar_bg_color = models.CharField(max_length=7, default='#1f2937', help_text='Hex color for light mode navbar background')
    light_navbar_text_color = models.CharField(max_length=7, default='#d1d5db', help_text='Hex color for light mode navbar text')
    dark_navbar_bg_color = models.CharField(max_length=7, default='#111827', help_text='Hex color for dark mode navbar background')
    dark_navbar_text_color = models.CharField(max_length=7, default='#f9fafb', help_text='Hex color for dark mode navbar text')

    light_footer_bg_color = models.CharField(max_length=7, default='#f9fafb', help_text='Hex color for light mode footer background')
    light_footer_text_color = models.CharField(max_length=7, default='#1f2937', help_text='Hex color for light mode footer text')
    dark_footer_bg_color = models.CharField(max_length=7, default='#111827', help_text='Hex color for dark mode footer background')
    dark_footer_text_color = models.CharField(max_length=7, default='#f9fafb', help_text='Hex color for dark mode footer text')

    light_intermediate_heading_color = models.CharField(max_length=7, default='#a3a3ff', help_text='Hex color for light mode intermediate headings')
    dark_intermediate_heading_color = models.CharField(max_length=7, default='#8b8bff', help_text='Hex color for dark mode intermediate headings')

    light_container_bg_color = models.CharField(max_length=7, default='#f5f0e9', help_text='Hex color for light mode container background')
    dark_container_bg_color = models.CharField(max_length=7, default='#1f2937', help_text='Hex color for dark mode container background')

    light_imageupload_container_bg_color = models.CharField(max_length=7, default='#1f2937', help_text='Hex color for light mode imageupload container background')
    dark_imageupload_container_bg_color = models.CharField(max_length=7, default='#111827', help_text='Hex color for dark mode imageupload container background')
    light_imageupload_text_color = models.CharField(max_length=7, default='#d1d5db', help_text='Hex color for light mode imageupload text color')
    dark_imageupload_text_color = models.CharField(max_length=7, default='#f9fafb', help_text='Hex color for dark mode imageupload text color')

    light_socialmedia_bg_color = models.CharField(max_length=7, default='#f5f0e9', help_text='Hex color for light mode socialmedia blog background')
    dark_socialmedia_bg_color = models.CharField(max_length=7, default='#1f2937', help_text='Hex color for dark mode socialmedia blog background')
    light_socialmedia_text_color = models.CharField(max_length=7, default='#000000', help_text='Hex color for light mode socialmedia blog text')
    dark_socialmedia_text_color = models.CharField(max_length=7, default='#d1d5db', help_text='Hex color for dark mode socialmedia blog text')

    light_socialmedia_links_text_color = models.CharField(max_length=7, default='#ffffff', help_text='Hex color for light mode socialmedia links text')
    dark_socialmedia_links_text_color = models.CharField(max_length=7, default='#d1d5db', help_text='Hex color for dark mode socialmedia links text')
    light_socialmedia_heading_text_color = models.CharField(max_length=7, default='#ffffff', help_text='Hex color for light mode socialmedia heading text')
    dark_socialmedia_heading_text_color = models.CharField(max_length=7, default='#d1d5db', help_text='Hex color for dark mode socialmedia heading text')

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
