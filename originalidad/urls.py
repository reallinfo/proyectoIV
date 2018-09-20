
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index),
    path('random/', include('aleatoriedad.urls')),
    path('admin/', admin.site.urls),
]
