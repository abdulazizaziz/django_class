from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'index.html')


def products(request):
    # products = Product.objects.all()
    products = Product.objects.filter(is_available=True)
    context = {
        "count": len(products),
        'products': products
    }

    # Other Quieries
    # iphone = Product.objects.get(id=1)
    # print(iphone.name)

    return render(request, 'products.html', context)