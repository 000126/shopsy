from ecommerceapp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('checkout/', views.checkout, name="checkout"),

]
