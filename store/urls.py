from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name="store") ,
    path('cart/',views.cart,name="cart") ,
    path('wish/',views.wish,name="wish") ,
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateitem,name="update_item"),
    path('updatewish/',views.updatewish,name="updatewish")
]