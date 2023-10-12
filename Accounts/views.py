from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Accounts.forms import User_login,sign_up
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>Home page>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""


def index(request):
    return render (request,'Index.html')

"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>About Us>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""

def Aboutus(request):
    return render(request,'About.html')


"""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Conatctus>>>>>>>>>>>>>>>>>>>>>>>>>
"""
def contact_us(request):
    return render(request,'Contactus.html')

def user_login(request):
    if request.method=='POST':
        user_login=User_login(request.POST)
        if user_login.is_valid():
            email=user_login.cleaned_data['Email']
            password=user_login.cleaned_data['password']
            user=authenticate(email=email,password=password)
            if user is not None:
              login(request,user)
              return redirect('index')
    else:
         user_login=User_login()
    return render(request,'Login.html',context={'admin':user_login})

def user_signup(request):
    if request.method=='POST':
        user_sign=sign_up(request.POST)
        if user_sign.is_valid():
          user_sign.save()
          user=authenticate(email=user_sign.cleaned_data['email'],password=user_sign.cleaned_data['password1'])
          login(request,user)
          user_sign=sign_up()
          return redirect('login')
    else:
        user_sign=sign_up()
    return render(request,'signup.html',context={'admin1':user_sign})

def user_logout(request):
    logout(request)
    return redirect('index')