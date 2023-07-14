from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    detail = models.TextField()
    
    def __str__(self):
        return self.name + ' --- ' + str(self.id)