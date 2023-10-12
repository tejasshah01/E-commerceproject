from django.contrib import admin
from products.models import products,category_brand
# Register your models here.

@admin.register(category_brand)
class category(admin.ModelAdmin):
    list_display=['id','Category']

@admin.register(products)
class Ecomm_products(admin.ModelAdmin):
    list_display=["id","Category","Item_name","Brand","Price"]


