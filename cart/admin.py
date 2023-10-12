from django.contrib import admin
from cart.models import cart_items
# Register your models here.
# @admin.register(cart)
# class Ecom_cart(admin.ModelAdmin):
#     list_display=["id","Customer","Total_price"]

@admin.register(cart_items)
class Ecom_cart_items(admin.ModelAdmin):
    list_display=["products"]
    