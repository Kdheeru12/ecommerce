from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
import random
import json
import datetime
from .models import *
from .utils import cookieCart,cartData,guestOrder
# Create your views here.
def homepage(request):
    """
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order= cookieData['order']
        items = cookieData['items']
    """
    data = cartData(request)
    cartItems = data['cartItems']
    order= data['order']
    items = data['items']
    products = Product.objects.all()
    context = {
        'products':products,
        'cartItems':cartItems,
    }
    return render(request,'category.html',context) 
def cart(request):
    """
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        print(order)
        print(created)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        print(cart)
        items =[]
        order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
        cartItems = order['get_cart_items']
        for i in cart:
            try:
                cartItems += cart[i]["quantity"]
                product = Product.objects.get(id=i)
                total = (product.price * cart[i]["quantity"])
                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]["quantity"]
                item = {
                    'product':{
                        'id':product.id,
                        'name':product.name,
                        'price':product.price,
                        'image':product.image,
                    },
                    "quantity":cart[i]['quantity'],
                    'get_total':total,
                }
                items.append(item)
                if product.avail == False:
                    order['shipping'] = True
            except:
                pass
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order= cookieData['order']
        items = cookieData['items']
        """
    data = cartData(request)
    cartItems = data['cartItems']
    order= data['order']
    items = data['items']
    context = {
        'items':items,
        'order':order,
        'cartItems':cartItems,
    }
    return render(request,'cart.html',context)
def updateItem(request):
    print('received')
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action',action)
    print('Actios',productId)
    customer=request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('item added',safe=False)
def checkout(request):
    """"
    if request.user.is_authenticated:
        customer=request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        print(order)
        print(created)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order= cookieData['order']
        items = cookieData['items']
    """
    data = cartData(request)
    cartItems = data['cartItems']
    order= data['order']
    items = data['items']
    context = {
        'items':items,
        'order':order,
        'cartItems':cartItems,
    }
    return render(request,'checkout.html',context)
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        """
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        
        if total == order.get_cart_total:
            order.complete = True
        order.save()
        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address =data['shipping']['address'],
                city =data['shipping']['city'],
                state =data['shipping']['state'],
                zipcode =data['shipping']['zipcode'],
            )
        """
    else:
        """
        print('not authenticated')
        print('COOKIES:',request.COOKIES)
        name = data['form']['name']
        email = data['form']['email']
        cookieData = cookieCart(request)
        items = cookieData['items']
        print('name:',name)
        print('email:',email)
        print('items:',items)
        customer,created = Customer.objects.get_or_create(
            email=email
        )
        customer.name = name
        customer.save()
        order = Order.objects.create(
            customer=customer,
            complete=False,
        )
        for item in items:
            product = Product.objects.get(id=item['product']['id'])
            OrderItem = OrderItem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity']
            )
        """
        customer,order = guestOrder(request,data)
    dat = cartData(request)
    ite = dat['items']
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    if total == order.get_cart_total:
        order.complete = True
        order.orderitems = str(ite)
        order.ordertotal = total
    order.save()
    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address =data['shipping']['address'],
            city =data['shipping']['city'],
            state =data['shipping']['state'],
            zipcode =data['shipping']['zipcode'],
        )
    return JsonResponse('payment completed',safe=False)
