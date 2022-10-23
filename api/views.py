# from django.shortcuts import render
# from rest_framework import viewsets
# from . import models, serializers
# # Create your views here.


# class ItemViewset(viewsets.ModelViewSet):

#     queryset = models.Item.objects.filter()

#     def get_serializer_class(self):
#         if self.action == 'list':
#             return serializers.ListItemsSerializer
#         if self.action == 'retrieve':
#             return serializers.SingleItemsSerializer
#         if self.action == "create":
#             return serializers.SingleItemsSerializer

#         return serializers.SingleItemsSerializer


# class BrandViewset(viewsets.ModelViewSet):

#     queryset = models.Brand.objects.filter()
#     serializer_class = serializers.ListBrandsSerializer


# class CategoryViewset(viewsets.ModelViewSet):

#     queryset = models.Category.objects.filter()
#     serializer_class = serializers.ListCategoriesSerializer
