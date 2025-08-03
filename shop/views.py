from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from decimal import Decimal
import stripe
import json
from .models import Product, DonationLog

# Set Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY

def shop_home(request):
    """
    Display all active products for donation
    """
    products = Product.objects.filter(is_active=True).order_by('price')
    return render(request, 'shop/home.html', {
        'products': products
    })

@login_required
def user_donation_history(request):
    """
    Display user's donation history with transaction IDs
    """
    donations = DonationLog.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/donation_history.html', {'donations': donations})

@login_required
def create_donation_session(request):
    """
    Create a Stripe checkout session for donation
    """
    if request.method == 'POST':
        try:
            product_id = request.POST.get('product_id')
            product = Product.objects.get(id=product_id, is_active=True)
            
            # Check if custom amount is provided
            custom_amount = request.POST.get('custom_amount')
            amount = Decimal(custom_amount) if custom_amount else product.price
            
            # Validate custom amount
            if custom_amount and (amount <= 0 or amount > 999999.99):
                messages.error(request, 'Invalid donation amount.')
                return redirect('shop:home')
            
            # Create a donation log entry with pending status
            donation_log = DonationLog.objects.create(
                product=product,
                user=request.user,
                amount=amount,
                currency=product.currency,
                status='pending'
            )
            
            # Get site settings for checkout styling
            try:
                from main.models import SiteSettings
                site_settings = SiteSettings.objects.first()
                if site_settings:
                    # Use light mode colors by default for Stripe checkout
                    primary_color = site_settings.light_intermediate_heading_color
                    background_color = site_settings.light_container_bg_color
                    text_color = site_settings.light_text_color
                    accent_color = site_settings.light_bg_color
                else:
                    primary_color = '#22c55e'  # Default green
                    background_color = '#ffffff'  # Default white
                    text_color = '#333333'
                    accent_color = '#cfd7df'
            except:
                primary_color = '#22c55e'  # Default green
                background_color = '#ffffff'  # Default white
                text_color = '#333333'
                accent_color = '#cfd7df'
            
            # Create Stripe checkout session
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card', 'bancontact', 'sofort'], # 'sepa_debit' 'giropay' 'ideal'
                line_items=[
                    {
                        'price_data': {
                            'currency': product.currency.lower(),
                            'product_data': {
                                'name': product.name,
                                'description': product.description,
                            },
                            'unit_amount': int(amount * 100),  # Convert to cents
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=request.build_absolute_uri('/shop/success/' + str(donation_log.id) + '/'),
                cancel_url=request.build_absolute_uri('/shop/'),
                metadata={
                    'donation_id': str(donation_log.id)
                }
            )
            
            return redirect(checkout_session.url, code=303)
            
        except Product.DoesNotExist:
            messages.error(request, 'Invalid product selected.')
            return redirect('shop:home')
        except Exception as e:
            messages.error(request, f'An error occurred while processing your donation: {str(e)}')
            return redirect('shop:home')
    
    return redirect('shop:home')

@login_required
def paypal_success(request):
    """
    Handle PayPal donation success callback
    """
    order_id = request.GET.get('orderID')
    product_id = request.GET.get('productID')
    
    if not order_id or not product_id:
        messages.error(request, 'Invalid PayPal donation data.')
        return redirect('shop:home')
    
    try:
        product = Product.objects.get(id=product_id, is_active=True)
        # For custom amount products, we'll use the price from the order details
        # In a real implementation, you would retrieve the actual amount from PayPal's API
        # For now, we'll use the product price as a fallback
        amount = product.price
        
        # Log the PayPal donation
        DonationLog.objects.create(
            product=product,
            user=request.user,
            amount=amount,
            currency=product.currency,
            status='completed',
            paypal_order_id=order_id
        )
        messages.success(request, 'Thank you for your PayPal donation!')
        return redirect('shop:donation_success', donation_id=DonationLog.objects.latest('id').id)
    except Product.DoesNotExist:
        messages.error(request, 'Invalid product selected.')
        return redirect('shop:home')

def donation_success(request, donation_id):
    """
    Display donation success page
    """
    try:
        donation = DonationLog.objects.get(id=donation_id)
        return render(request, 'shop/donation_success.html', {'donation': donation})
    except DonationLog.DoesNotExist:
        messages.error(request, 'Donation record not found.')
        return redirect('shop:home')

@csrf_exempt
def stripe_webhook(request):
    """
    Handle Stripe webhook events
    """
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        
        # Update donation log status
        try:
            donation_id = session['metadata']['donation_id']
            donation = DonationLog.objects.get(id=donation_id)
            donation.status = 'completed'
            donation.stripe_payment_intent_id = session.get('payment_intent', '')
            donation.save()
        except DonationLog.DoesNotExist:
            return HttpResponse(status=404)

    return HttpResponse(status=200)


def test_copy(request):
    return render(request, 'shop/test_copy.html')
