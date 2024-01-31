from products.models import Product
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
class Cart:
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product, quantity=1, replcace_quantity=False):
        """
        Add the specified product to cart if is not exists else add the quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart.keys():
            self.cart[product_id] = {
                'quantity': 0
            }
        if replcace_quantity:
            # replace the current quantity with new one
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        messages.success(self.request, _("Your cart has been Updated successfully"))
        self.save()

    def save(self):
        """
        Marks that session was changed
        """
        self.session.modified = True 

    def delete(self, product):
        """
        Remove a product from cart 
        """
        product_id = product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['product_obj'].price * item['quantity']
            yield item
    
    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        # product_ids = self.cart.keys() 
        # products = Product.objects.filter(id__in=product_ids)
        return sum(item['product_obj'].price * item['quantity'] for item in self.cart.values())
