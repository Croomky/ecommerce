from django.contrib import admin
from django.urls import path
from .views import CategoryList, CategoryDetails, FeaturedProducts
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('category', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetails.as_view()),
    path('product/featured/', FeaturedProducts.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
