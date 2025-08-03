from django.conf import settings
from main.models import SiteSettings

def shop_context(request):
    # Get site settings for color customization
    try:
        site_settings = SiteSettings.objects.first()
    except SiteSettings.DoesNotExist:
        site_settings = None
    
    context = {
        'PAYPAL_CLIENT_ID': getattr(settings, 'PAYPAL_CLIENT_ID', ''),
        'STRIPE_PUBLISHABLE_KEY': getattr(settings, 'STRIPE_PUBLISHABLE_KEY', ''),
    }
    
    # Add color settings to context if available
    if site_settings:
        context.update({
            'light_container_bg': site_settings.light_container_bg_color,
            'dark_container_bg': site_settings.dark_container_bg_color,
            'light_text': site_settings.light_text_color,
            'dark_text': site_settings.dark_text_color,
        })
    
    return context
