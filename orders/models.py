from django.db import models
from Accounts.models import User
from products.models import products
from cart.models import cart_items

# Create your models here.

class order(models.Model):
    Customer=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField('cart.cart_items')
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.BigIntegerField()
    Location=models.CharField(max_length=50)
    Shipping_address=models.CharField(max_length=100)
    Total_price=models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    is_paid=models.BooleanField(default=False)

    

    
    

