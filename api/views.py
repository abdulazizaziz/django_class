from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from .serializers import ProductSerializer

@api_view(['GET', 'POST', 'DELETE'])
def products(request):
    print(request.method)
    if request.method == 'POST':
        create_serializer = ProductSerializer(data=request.data)
        if create_serializer.is_valid():
            create_serializer.save()
        else:
            return Response(create_serializer.errors)
        # name = request.data['name']
        # price = request.data['price']
        # category = request.data['category']
        # detail = request.data['detail']
        # is_available = request.data['is_available']
        # Product.objects.create(name=name, price=price, category_id=category, detail=detail, is_available=is_available)
    # elif request.method == 'DELETE':
    #     product = Product.objects.get(id=14)
    #     product.delete()


    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
