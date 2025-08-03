from django.conf import settings

def shop_context(request):
    return {
        'PAYPAL_CLIENT_ID': settings.PAYPAL_CLIENT_ID,
        'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
    }
