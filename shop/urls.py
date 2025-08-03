from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_home, name='home'),
    path('history/', views.user_donation_history, name='donation_history'),
    path('donate/', views.create_donation_session, name='create_donation_session'),
    path('success/<int:donation_id>/', views.donation_success, name='donation_success'),
    path('paypal-success/', views.paypal_success, name='paypal_success'),
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
    # path('test-copy/', views.test_copy, name='test_copy'),
]
