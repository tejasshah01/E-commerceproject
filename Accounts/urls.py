from django.contrib import admin
from django.urls import path
from Accounts.views import user_login,user_signup,Aboutus,user_logout,contact_us

urlpatterns =[
    path('login/',user_login,name='login'),
    path('signup/',user_signup,name='signup'),
    path('logout',user_logout,name='logout'),
    path('Aboutus',Aboutus,name='About'),
    path('contact_us',contact_us,name='contact')
   
]