from django.contrib import admin

from cart.models import CartItem
from order.models import Order, OrderItem
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)