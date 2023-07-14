from django.contrib import admin
from django.urls import path
from products.views import home, students


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('students/', students)
]
