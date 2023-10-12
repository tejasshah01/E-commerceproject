from django.db import models
#custom user
from django.contrib.auth.models import AbstractUser
#import username
from Accounts.UserManager import userManager
# Create your models here.
# """
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Business logic>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# """

class User(AbstractUser):
    user_type_choice=[
          ('admin','Admin')
     ]
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=False )
    email=models.EmailField(unique=True)
    phone=models.CharField(unique=True,max_length=100)
     # password=models.CharField(max_length=100)
    user_type=models.CharField(max_length=50,choices=user_type_choice,default='admin')
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    last_login=models.DateTimeField(blank=True,null=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

     #images
    profile_image=models.ImageField(upload_to='user_profile',null=True)

     #required field for django login
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','phone']
    objects=userManager()

    def __str__(self) :
        return f"{self.first_name}-{self.email}"










class user_account(models.Model):
    Name=models.CharField(max_length=100)
    Contact_No=models.CharField(max_length=20)
    user_id=models.CharField(unique=True,max_length=20)
    Email_id=models.EmailField(unique=True)
    Password=models.CharField(max_length=20)
    is_active=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Name}-{self.Contact_No}"

 
    

