from django.contrib import admin
from django.urls import path, include
from products.views import home, products, create_product, delete_product


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('products/', products),
    path('createproducts/', create_product),
    path('deleteproducts/', delete_product),
    path("__debug__/", include("debug_toolbar.urls")),
]
