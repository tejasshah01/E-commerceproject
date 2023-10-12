from django.contrib import admin
from shipping.models import shipping
# Register your models here.
@admin.register(shipping)
class Customer_address(admin.ModelAdmin):
    list_display=["id","customer","state","city","pincode","Location"]
