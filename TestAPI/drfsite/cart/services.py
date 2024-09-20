from cart.models import CartItem
from catalog.models import Product


class CartsService:

    def __init__(self, **data):
        self.data = data

    def get_cart(self):
        queryset = CartItem.objects.filter(user_id=self.data.get('user_id'))
        return queryset

    def post_item(self):
        cart = CartItem(

            product_id=self.data['product_id'],
            quantity=self.data['quantity'],
            user_id=self.data['user_id']
        )
        cart.save()
        return self.get_cart()

    def put_item(self):
        curr_item = CartItem.objects.get(user_id=self.data['user_id'], product_id=self.data['product_id'])
        curr_item.quantity = self.data['quantity']
        curr_item.save()
        return self.get_cart()

    def delete_item(self):
        curr_item = CartItem.objects.get(user_id=self.data['user_id'], product_id=self.data['product_id'])
        curr_item.delete()
        return self.get_cart()
