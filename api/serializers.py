from rest_framework import serializers
from products.models import Product


# class ProductSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     price = serializers.IntegerField()
#     detail = serializers.CharField()
#     is_available = serializers.BooleanField()
#     category = serializers.IntegerField(write_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = [
            'id',
            'name'
        ]