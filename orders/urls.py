from django.contrib import admin
from django.urls import path
from orders.views import place_order,order_details

urlpatterns = [
    path('place_order',place_order,name='placed'),
    path('order_info',order_details,name='order')

]