from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration),
    path('sign-in/', views.sign_in),
    path('logout/', views.logout)

]