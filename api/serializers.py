# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from items import models

# User = get_user_model()


# class ListUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"

#         extra_kwargs = {
#             'password': {'write_only': True},
#             # 'another_field': {'read_only': True}
#         }


# class ListBrandsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Brand
#         fields = "__all__"


# class ListCategoriesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Category
#         fields = "__all__"


# class ListItemsSerializer(serializers.ModelSerializer):
#     brand = ListBrandsSerializer(read_only=True)
#     category = ListCategoriesSerializer(read_only=True)

#     class Meta:

#         model = models.Item
#         fields = "__all__"
# class SingleItemsSerializer(serializers.ModelSerializer):

#     class Meta:

#         model = models.Item
#         fields = "__all__"