from django.contrib import admin
from django.urls import path, include
from products.views import home, products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('products/', products),
    path("__debug__/", include("debug_toolbar.urls")),
]
