from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from inventory.models import Category, Product
from inventory.serializers import CategoryListSerializer, ProductListSerializer
# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
