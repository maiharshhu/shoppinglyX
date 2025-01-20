from django.contrib import admin
from .models import (Customer, Product, Cart, OrderPlace)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name',
                    'locality', 'city', 'zipcode', 'state']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price',
                    'discounted_price', 'brand', 'category', 'product_image']
    list_filter = ['category', 'brand']
    search_fields = ['title', 'brand', 'category']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
    list_filter = ['user']
    search_fields = ['user__username', 'product__title']


@admin.register(OrderPlace)
class OrderPlaceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product',
                    'quantity', 'price', 'status', 'order_date', 'updated_at']
    list_filter = ['status', 'order_date', 'updated_at']
    search_fields = ['user__username',
                     'customer__name', 'product__title', 'status']
