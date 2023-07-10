from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    detail = models.TextField()
    is_available = models.BooleanField(default=True)

    color = models.CharField(max_length=30, null=True, blank=True)

    added = models.DateField(auto_now_add=True)