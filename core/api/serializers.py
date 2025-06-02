from rest_framework import serializers
from core.pos.models import Category, Product, Client


# muy parecido a la definicion de forms

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def to_representation(self, instance):
        return instance.toJSON()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        return instance.toJSON()