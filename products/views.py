from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import Product

from django.core.exceptions import ObjectDoesNotExist

def main(request):
    return HttpResponseRedirect('/home/')

def home(request):
    return render(request, 'index.html')


def products(request):
    products = Product.objects.all()
    # products = Product.objects.filter(is_available=True)
    context = {
        "count": len(products),
        'products': products
    }

    # Other Quieries
    # iphone = Product.objects.get(id=1)
    # print(iphone.name)

    return render(request, 'products.html', context)

    
def create_product(request):
    # print(request.method)
    # print(request.GET)
    # print(dict(request.GET))
    # print(request.POST)
    name = request.POST['name']
    price = request.POST['price']
    detail = request.POST['detail']
    if 'is_available' in request.POST:
        is_available = True
    else:
        is_available = False
    
    Product.objects.create(name=name, price=price, detail=detail, is_available=is_available)

    return HttpResponseRedirect('/products')

def delete_product(request):
    try:
        item = Product.objects.get(id=request.GET['id'])
        item.delete()
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect('/products')


def edit_product(request, id):
    try:
        item = Product.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/products')
    return render(request, 'editproduct.html', {"product": item})

def update_product(request, id):
    try:
        item = Product.objects.get(id=id)
        # print(request.POST)
        name = request.POST['name']
        price = request.POST['price']
        detail = request.POST['detail']
        is_available = request.POST.get('is_available')
        
        item.name = name
        item.price = price
        item.detail = detail
        if is_available:
            item.is_available = True
        else:
            item.is_available = False
        item.save()


    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect('/products') 