from django.db import models
from Accounts.models import User
from products.models import products

# Create your models here.


# class cart(models.Model):
   
#     Total_price=models.DecimalField(max_digits=20,decimal_places=2)
#     discount=models.DecimalField(max_digits=10,decimal_places=2)
#     Final_price=models.DecimalField(max_digits=20,decimal_places=2)
#     created_on=models.DateTimeField(auto_now_add=True)
#     Updated_on=models.DateTimeField(auto_now=True)
#     Checked_out=models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.discount}" 


class cart_items(models.Model):
    products=models.ForeignKey(products,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)


    def __str__(self) -> str:
        return f"{self.products}"

    

