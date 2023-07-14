from django.shortcuts import render
from .models import Product


def home(request):
    return render(request, 'index.html')


def students(request):
    products = Product.objects.all()
    context = {
        "count": len(products),
        'products': products
    }
    return render(request, 'students.html', context)