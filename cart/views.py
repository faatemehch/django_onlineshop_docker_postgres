from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from products.models import Product
from .forms import AddToCartForm


def cart_detail_view(request):
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'cart/cart_detail.html', context)


def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        # the form has validated - we can add to the cart
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity) # request.session.modified = True  # marks that session was changed
    return redirect('cart:cart_detail')
