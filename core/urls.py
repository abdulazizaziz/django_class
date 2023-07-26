from django.contrib import admin
from django.urls import path, include
# from products.views import home, products, create_product, delete_product, edit_product, update_product, main
from products.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('home/', home),
    path('products/', products),
    path('createproducts/', create_product),
    path('deleteproducts/', delete_product),
    path('products/<int:id>/', edit_product),
    path('updateproducts/<int:id>/', update_product),

    path('categories/', categories),
    path('categories/<int:id>/', category_edit),
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)