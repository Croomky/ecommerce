from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('authenticate', views.signin, name='signin'),
    path('activate/<code>', views.activate),
    path('profile', views.userProfile, name='profile'),
    path('signout', views.signout, name='signout'),
    path('profile-info', views.ProfileInfo.as_view(), name='profileInfo'),
]