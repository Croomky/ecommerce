from django.contrib import admin
from django.urls import path
from .views import CategoryList, CategoryDetails, FeaturedProducts, ProductDetails, ProductList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('category', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetails.as_view()),
    path('product/featured/', FeaturedProducts.as_view()),
    path('product/details/<int:pk>', ProductDetails.as_view(), name="productDetails"),
    path('product', ProductList.as_view(), name="products")
]

urlpatterns = format_suffix_patterns(urlpatterns)
