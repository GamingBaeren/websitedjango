from django.contrib import admin
from .models import Product, DonationLog

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency', 'allow_custom_amount', 'is_active', 'created_at')
    list_filter = ('is_active', 'allow_custom_amount', 'currency', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('is_active',)

@admin.register(DonationLog)
class DonationLogAdmin(admin.ModelAdmin):
    list_display = ('product', 'amount', 'currency', 'user', 'status', 'created_at')
    list_filter = ('status', 'currency', 'created_at')
    search_fields = ('product__name', 'user__username', 'stripe_payment_intent_id')
    readonly_fields = ('created_at',)
    
    # Allow filtering by date
    date_hierarchy = 'created_at'
