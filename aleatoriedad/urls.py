
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.test),
    path('random_number', views.random_number),
]
