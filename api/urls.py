from django.urls import path
from rest_framework.routers import DefaultRouter
from inventory.views import CategoryViewSet, ProductViewSet

router = DefaultRouter()

router.register("products", ProductViewSet, basename="products")
router.register("categories", CategoryViewSet, basename="categories")
# router.register("categories", views.CategoryViewset, basename="categories")
# router.register("brands", views.BrandViewset, basename="brands")
urlpatterns = [
    # path()
]

urlpatterns += router.urls
