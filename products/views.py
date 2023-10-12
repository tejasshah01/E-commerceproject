from django.shortcuts import render
from products.models import category_brand,products
from django.views import View
from django.shortcuts import redirect
from cart.models import cart_items
from django.contrib.auth.decorators import login_required



class add_to_cart(View):
    # def post(self , request):
    #     product = request.POST.get('product')
    #     remove = request.POST.get('remove')
    #     cart = request.session.get('cart')
    #     if cart:
    #         quantity = cart.get(product)
    #         if quantity:
    #             if remove:
    #                 if quantity>=1:
    #                     cart.pop(product)
    #                 else:
    #                     cart[product]  = quantity-1
    #             else:
    #                 cart[product]  = quantity+1

    #         else:
    #             cart[product] = 1
    #     else:
    #         cart = {}
    #         cart[product] = 1

    #     request.session['cart'] = cart
    #     print('cart' , request.session['cart'])
    #     return redirect('category')
    def get(self,request):
        Products=None
        
        categories=category_brand.get_all_categories()
        categoryID=request.GET.get('category')
        if categoryID:
           Products=products.get_all_products_by_categoryid(categoryID)
        else:
           Products=products.get_all_products()
        data={}
        data['categories']=categories
        return render(request,'Shop.html',context={'collections':Products,'category_items':categories})



    # category=category_brand.objects.all()
    # collections=products.objects.all()
@login_required(login_url='login')
def index(request):
    
    Product= products.objects.all()
    cart_list = cart_items.objects.all()
    return render(request,'Shop.html',context={
        'collections':Product,
        'cart_list':cart_list
    })

@login_required(login_url='login')
def cart(request):
    summ = 0
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        my_prod = products.objects.get(id=prod_id)
        cart_items.objects.create(products=my_prod)
        return redirect('category')
    
    cart_list = cart_items.objects.all()
    cart_sum = cart_items.objects.all()
    for i in cart_sum:
        summ += i.products.Price
    
    return render(request,'checkout.html',context={'cart_list':cart_list, 'summ':summ})


def delete_item(request):
    if request.method == 'POST':
        prod_id = request.POST.get('id')
        cart_items.objects.filter(id=prod_id).delete()
        return redirect('cart')
    



