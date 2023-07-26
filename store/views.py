from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
# Create your views here.

def store(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems=order['get_cart_items']

    context={'products':products,'cartItems':cartItems}
    return render(request,'store/store.html',context)


def cart(request):

    if request.user.is_authenticated:
        customer=request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems=order['get_cart_items']


    context={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)


def wish(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        wish,created=Wish.objects.get_or_create(customer=customer)
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items=wish.wishitem_set.all()
        cartItems=order.get_cart_items
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_items':0}
        cartItems=order['get_cart_items']


    context={'items':items,'wish':wish,'cartItems':cartItems}
    return render(request,'store/wish.html',context)


def checkout(request):
    context={}
    return render(request,'store/checkout.html',context)

def updateitem(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print(action,productId)

    customer=request.user.customer
    product=Product.objects.get(id=productId)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)

    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
    elif action=='remove':
        orderItem.quantity=(orderItem.quantity-1)
    # elif action=='delete':
    #     orderItem.delete()

    orderItem.save()

    if orderItem.quantity<=0 or action=='delete':
        orderItem.delete()



    return JsonResponse('Item was added',safe=False)


def updatewish(request):
    data=json.loads(request.body)
    productId=data['productId']
    action=data['action']
    print(action,productId)

    customer=request.user.customer
    product=Product.objects.get(id=productId)
    wish,created=Wish.objects.get_or_create(customer=customer)
    items,created=WishItem.objects.get_or_create(wish=wish,product=product)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)

    if action=='add':
        orderItem.quantity=(orderItem.quantity+1)
        items.delete()
    elif action=='delete':
        items.delete()
    elif action=='append':
        items+=orderItem

    # elif action=='remove':
    #     orderItem.quantity=(orderItem.quantity-1)
    #  elif action=='delete':
    #      orderItem.delete()
    orderItem.save()

    # if orderItem.quantity<=0 or action=='delete':
        # orderItem.delete()



    return JsonResponse('Item was added',safe=False)
