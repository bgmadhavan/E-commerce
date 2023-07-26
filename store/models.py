from django.db import models as m
from django.contrib.auth.models import User
# Create your models here.

class Customer(m.Model):
    user = m.OneToOneField(User,null=True,blank=True,on_delete=m.CASCADE)
    name = m.CharField(max_length=200,null=True)
    email = m.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(m.Model):
    name=m.CharField(max_length=200,null=True)
    price=m.FloatField()
    image=m.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name
    
class Order(m.Model):
    customer = m.ForeignKey(Customer,on_delete=m.SET_NULL,blank=True,null=True)
    date=m.DateTimeField(auto_now_add=True)
    complete=m.BooleanField(default=False,null=True,blank=False)
    trans_id=m.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems=self.orderitem_set.all()
        total=sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(m.Model):
    product=m.ForeignKey(Product,on_delete=m.SET_NULL,null=True)
    order=m.ForeignKey(Order,on_delete=m.SET_NULL,null=True)
    quantity=m.IntegerField(default=0,null=True,blank=True)
    date_added=m.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total=self.product.price * self.quantity
        return total


class Wish(m.Model):
    customer = m.ForeignKey(Customer,on_delete=m.SET_NULL,blank=True,null=True)
    date=m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_items(self):
        orderitems=self.wishitem_set.all()
        total=len(orderitems)
        return total
    
class WishItem(m.Model):
    product=m.ForeignKey(Product,on_delete=m.SET_NULL,null=True)
    wish=m.ForeignKey(Wish,on_delete=m.SET_NULL,null=True)
    date_added=m.DateTimeField(auto_now_add=True)


