import datetime

from cart.models import CartItem
from django.conf import settings
from order.models import Order, OrderItem
from dadata import Dadata


class OrderService:

    def __init__(self, **data):
        self.data = data

    def create_order(self):
        address_query = self.data['client_adress']
        address = self.get_address_suggestions(address_query)
        self.data['address'] = address[0]['value']

        order = Order(
            user_id = self.data['user_id'],
            created_at = datetime.datetime.now(),
            address = self.data.get('address')
        )
        order.save()
        self.add_orderitems(order.id)
        cart = CartItem.objects.filter(user_id = self.data['user_id'])
        cart.delete()

    def add_orderitems(self, order_id):
        order_items = []
        cart_items = CartItem.objects.filter(user_id = self.data.get('user_id'))
        for item in cart_items:
            order_item = OrderItem(
                order_id = order_id,
                product_id=item.product_id,
                quantity=item.quantity
            )
            order_items.append(order_item)
        OrderItem.objects.bulk_create(order_items, batch_size=1000)

    def get_address_suggestions(self, query):
        token = settings.TOKEN
        dadata = Dadata(token)
        result = dadata.suggest("address", query)
        return result
