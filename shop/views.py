from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
import random
from .models import *


# Create your views here.
def homepage(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'category.html',context) 
def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        print(order)
        print(created)
        items = order.orderitem_set.all()
    else:
        items =[]
        order = {'get_cart_total':0}
    context = {
        'items':items,
        'order':order,
    }
    return render(request,'cart.html',context)
def updateItem(request):
    return JsonResponse('item added',safe=False)
