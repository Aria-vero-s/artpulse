from django.shortcuts import render
from django.urls import path 
from . import views

urlpatterns = [
# Add this line of code for all your URLs (i.e about.html, contact.html, etc.)
    path('', views.index, name='index'),
]