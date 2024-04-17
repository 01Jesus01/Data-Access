from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('', views.index)
]