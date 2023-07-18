from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .models import Product

from django.core.exceptions import ObjectDoesNotExist


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
