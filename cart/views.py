from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from products.models import Product
from .forms import AddToCartForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item["product_update_quantity_form"] = AddToCartForm(initial={
            'quantity': item['quantity'],
            'inplace': True
        })
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart_detail.html', context)


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        # the form has validated - we can add to the cart
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, cleaned_data['inplace'])
    return redirect('cart:cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.delete(product)
    return redirect('cart:cart_detail')


@require_POST
def clear_cart(request):
    cart = Cart(request)
    if len(cart) != 0:
        cart.clear()
        messages.success(request, _("Your cart has been deleted succesfully"))
    else:
        messages.warning(request, _("Your cart is already empty."))
    return redirect("product_list")   
