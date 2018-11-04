from django.contrib import admin
from django.urls import path
from .views import CategoryList, CategoryDetails
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', CategoryList.as_view()),
    path('<int:pk>/', CategoryDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
