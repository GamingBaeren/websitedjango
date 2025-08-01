from .models import SiteSettings

def dark_mode(request):
    dark_mode_enabled = request.COOKIES.get('dark_mode', 'false') == 'true'
    try:
        settings = SiteSettings.objects.first()
    except SiteSettings.DoesNotExist:
        settings = None

    if settings:
        light_bg = settings.light_bg_color
        light_text = settings.light_text_color
        dark_bg = settings.dark_bg_color
        dark_text = settings.dark_text_color

        light_navbar_bg = settings.light_navbar_bg_color
        light_navbar_text = settings.light_navbar_text_color
        dark_navbar_bg = settings.dark_navbar_bg_color
        dark_navbar_text = settings.dark_navbar_text_color

        light_footer_bg = settings.light_footer_bg_color
        light_footer_text = settings.light_footer_text_color
        dark_footer_bg = settings.dark_footer_bg_color
        dark_footer_text = settings.dark_footer_text_color
    else:
        light_bg = '#f5f0e9'
        light_text = '#000000'
        dark_bg = '#000000'
        dark_text = '#d1d5db'

        light_navbar_bg = '#1f2937'
        light_navbar_text = '#d1d5db'
        dark_navbar_bg = '#111827'
        dark_navbar_text = '#f9fafb'

        light_footer_bg = '#f9fafb'
        light_footer_text = '#1f2937'
        dark_footer_bg = '#111827'
        dark_footer_text = '#f9fafb'

    return {
        'dark_mode_enabled': dark_mode_enabled,
        'light_bg': light_bg,
        'light_text': light_text,
        'dark_bg': dark_bg,
        'dark_text': dark_text,
        'light_navbar_bg': light_navbar_bg,
        'light_navbar_text': light_navbar_text,
        'dark_navbar_bg': dark_navbar_bg,
        'dark_navbar_text': dark_navbar_text,
        'light_footer_bg': light_footer_bg,
        'light_footer_text': light_footer_text,
        'dark_footer_bg': dark_footer_bg,
        'dark_footer_text': dark_footer_text,
    }
