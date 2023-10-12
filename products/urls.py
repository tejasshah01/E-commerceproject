from django.contrib import admin
from django.urls import path
from products.views import add_to_cart,cart,delete_item

urlpatterns = [
 
     path('add_to_cart',add_to_cart.as_view(),name='category'),
     path('cart',cart,name='cart'),
     path('delete_item',delete_item,name='delete')
  
]

