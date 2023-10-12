from django.db import models
from Accounts.models import User
from orders.models import order
from cart.models import cart_items
# Create your models here.
class shipping(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    order=models.ForeignKey(cart_items,on_delete=models.CASCADE,default=1)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.BigIntegerField()
    Location=models.CharField(max_length=50)
    Shipping_address=models.CharField(max_length=100)


class ship_details(models.Model):
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.BigIntegerField()
    Location=models.CharField(max_length=50)
    Shipping_address=models.CharField(max_length=100)
