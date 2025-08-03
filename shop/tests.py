from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from unittest.mock import patch, MagicMock
from decimal import Decimal
from main.models import SiteSettings
from shop.models import Product, DonationLog

class ShopTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            description='Test product for donation',
            price=Decimal('10.00'),
            currency='EUR',
            is_active=True
        )
        
        # Create site settings for testing
        self.site_settings = SiteSettings.objects.create(
            site_name='Test Site',
            light_bg_color='#f5f0e9',
            light_text_color='#000000',
            dark_bg_color='#000000',
            dark_text_color='#d1d5db',
            light_intermediate_heading_color='#a3a3ff',
            dark_intermediate_heading_color='#8b8bff',
            light_container_bg_color='#f5f0e9',
            dark_container_bg_color='#1f2937'
        )
        
        # Create a test client
        self.client = Client()
        self.client.login(username='testuser', password='testpass123')

    def test_shop_home_view(self):
        """Test that the shop home page loads correctly"""
        response = self.client.get(reverse('shop:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Support Us with a Donation')
        self.assertContains(response, self.product.name)

    @patch('shop.views.stripe.checkout.Session.create')
    def test_create_donation_session_with_styling(self, mock_stripe_create):
        """Test that creating a donation session includes styling from site settings"""
        # Mock the Stripe checkout session creation
        mock_session = MagicMock()
        mock_session.url = 'https://checkout.stripe.com/test'
        mock_stripe_create.return_value = mock_session
        
        # Post to create donation session
        response = self.client.post(reverse('shop:create_donation_session'), {
            'product_id': self.product.id
        })
        
        # Check that Stripe session was called with appearance settings
        mock_stripe_create.assert_called_once()
        args, kwargs = mock_stripe_create.call_args
        
        # Verify appearance settings are included
        self.assertIn('appearance', kwargs)
        appearance = kwargs['appearance']
        self.assertIn('variables', appearance)
        self.assertIn('colorPrimary', appearance['variables'])
        self.assertIn('colorBackground', appearance['variables'])
        
        # Verify the colors match site settings
        self.assertEqual(appearance['variables']['colorPrimary'], '#a3a3ff')
        self.assertEqual(appearance['variables']['colorBackground'], '#f5f0e9')

    def test_donation_history_view(self):
        """Test that the donation history page loads correctly"""
        # Create a test donation log
        DonationLog.objects.create(
            product=self.product,
            user=self.user,
            amount=Decimal('10.00'),
            currency='EUR',
            status='completed'
        )
        
        response = self.client.get(reverse('shop:donation_history'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Donation History')
        self.assertContains(response, self.product.name)

    def test_shop_context_processor(self):
        """Test that the shop context processor includes necessary settings"""
        response = self.client.get(reverse('shop:home'))
        
        # Check that PayPal and Stripe keys are in context
        self.assertIn('PAYPAL_CLIENT_ID', response.context)
        self.assertIn('STRIPE_PUBLISHABLE_KEY', response.context)
        
        # Check that color settings are in context
        self.assertIn('light_container_bg', response.context)
        self.assertIn('dark_container_bg', response.context)
        self.assertIn('light_text', response.context)
        self.assertIn('dark_text', response.context)
