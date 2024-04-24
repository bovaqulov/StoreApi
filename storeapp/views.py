from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductList(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


"""
# barcha Maxsulotlar
https://storeus.pythonanywhere.com/api/v1/products/

# bitta maxsulot uchun  
https://storeus.pythonanywhere.com/api/v1/products/9


#barcha categoriyalar
https://storeus.pythonanywhere.com/api/v1/categories/


# bitta categoriya
https://storeus.pythonanywhere.com/api/v1/categories/1

# sayit
https://storeus.pythonanywhere.com/admin

username: admin1 yoki admin
parol: 123

"""