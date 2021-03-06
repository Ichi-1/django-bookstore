from decimal import Decimal
from apps.checkout.models import DeliveryOptions
from apps.store.models import Product


class Basket():
    """
    Base Basket Class, prodiving default behaviors that
    can be inreritated or orverride, as necessary.
    """
    # if user is new on our site, then user havent session
    # and
    # we need to build new session for user

    def __init__(self, request):
        # getting a session object from request object
        self.session = request.session

        # resotre basket data if session exist
        basket = self.session.get('basket_id')

        if 'basket_id' not in request.session:
            # basket session is empty dict
            basket = self.session['basket_id'] = {}

        # instantiating basket based on basket_id exist or not
        self.basket = basket

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        # add to basket product data attr based on filter result
        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

    def save(self):
        """
        By default, Django only saves to the session database
        when the session has been modified
        """
        self.session.modified = True

    def add(self, product, qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {
                'price': str(product.regular_price),
                'qty': qty
            }
        self.save()

    def delete(self, product_id):
        """
        Delete item from session data
        """
        product_id = str(product_id)

        if product_id in self.basket:
            del self.basket[product_id]
        self.save()

    def update(self, product_id, qty):
        """
        Update values in sessions data
        """
        # type cast
        product_id = str(product_id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
            self.save()

    def clear(self):
        del self.session['basket_id']
        del self.session['address']
        del self.session['delivery']

        self.save()

    def get_subtotal_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def get_total_price(self):
        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

        delivery_price = 0.00

        if 'delivery' in self.session:
            delivery_id = self.session['delivery']['delivery_id']
            delivery_price = DeliveryOptions.objects.get(id=delivery_id).price

        total = subtotal + Decimal(delivery_price)
        return total

    def get_delivery_price(self):
        delivery_price = 0.00

        if 'delivery' in self.session:
            delivery_id = self.session['delivery']['delivery_id']
            delivery_price = DeliveryOptions.objects.get(id=delivery_id).price
        return delivery_price


    def update_total_price(self, delivery_price=0):
        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())
        updated_total = subtotal + Decimal(delivery_price)
        return updated_total
