"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""


from django.contrib import admin
from django.urls import path,include,re_path
from .import views
from django.conf.urls import url, include
from django.conf import settings

urlpatterns = [
    path('',views.homepage,name='home'),
    path('cart',views.cart,name='cart'),
    path('update_item/',views.updateItem,name='updateitems'),
    path('checkout/',views.checkout,name='checkout'),
    path('process_order/',views.processOrder,name='processorder'),
    path('my',views.myaccount,name='myaccount')
]