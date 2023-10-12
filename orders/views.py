from django.shortcuts import render
from orders.models import order
from cart.models import cart_items
from orders.forms import ship_form
from django.shortcuts import redirect

# Create your views here.

def place_order(request):
    products=123
    user_cart=cart_items.objects.filter(products=products)
    if request.method=='POST':
        form=ship_form(request.POST)
        if form.is_valid():
            state=form.cleaned_data['state']
            city=form.cleaned_data['city']
            pincode=form.cleaned_data['pincode']
            Location=form.cleaned_data['Location']
            Shipping_address=form.cleaned_data['Shipping_address']
            Order=order(Customer=request.user,state=state,city=city,pincode=pincode,Location=Location,Shipping_address=Shipping_address)
            Order.save()
            return redirect('category')
    else:
            form=ship_form()
    return render(request,'shipping.html',context={'form':form})


def order_details(request):
     order_info=order.objects.filter(is_paid=True)
     return render(request,'order.html',context={'order_info':order_info})



