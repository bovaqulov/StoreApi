from rest_framework import serializers
from .models import Product, Option, Gallery, Category, Color


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['key', "value"]


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['image']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name']

class ProductSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)
    galleries = GallerySerializer(many=True)
    colors = ColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', "price", "category", 'description','colors', 'options', 'galleries']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
