import datetime

from cart.models import CartItem
from order.models import Order, OrderItem


class OrderService:

    def __init__(self, **data):
        self.data = data

    def create_order(self):
        order = Order(
            user_id = self.data['user_id'],
            created_at = datetime.datetime.now()
        )
        order.save()
        self.add_orderitems(order.id)
        cart = CartItem.objects.filter(user_id = self.data['user_id'])
        cart.delete()

    def add_orderitems(self, order_id):
        cart_items = CartItem.objects.filter(user_id = self.data.get('user_id'))
        for item in cart_items:
            order_item = OrderItem(
                order_id = order_id,
                product_id=item.product_id,
                quantity=item.quantity
            )
            order_item.save()
