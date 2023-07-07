from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    detail = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    about = models.CharField(max_length=50, null=True)
    added = models.DateField(auto_now_add=True)