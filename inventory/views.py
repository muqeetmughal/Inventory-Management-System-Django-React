from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from inventory.models import Product
from inventory.serializers import ProductListSerializer
# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
