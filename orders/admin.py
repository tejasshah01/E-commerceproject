from django.contrib import admin
from orders.models import order
# Register your models here.
@admin.register(order)
class Ecomm_order(admin.ModelAdmin):
    list_display=["id","Customer"]

