from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name', 'id']

    def __str__(self):
        return self.name + ' --- ' + str(self.id)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    detail = models.TextField()
    # category = models.ForeignKey('products.Category', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE)

    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + ' --- ' + str(self.id)