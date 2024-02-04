from django.db import models
# from django.contrib.auth import get_user_model
from django.conf import settings
from products.models import Product
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name=_("User"))
    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"),max_length=100)
    phone_numbe = models.CharField(_("Phone Number"), max_length=15)
    address = models.CharField(_("Address"),max_length=700)
    is_paid = models.BooleanField(_("Is Paide"), default=False)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True)
    order_note = models.CharField(_("Order Note"), max_length=700, blank=True)
    def __str__(self):
        return f"Order {self.id}"
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_('Order'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name=_("Product"))
    quantity = models.PositiveIntegerField(default=1, verbose_name=_("Quantity"))
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"OrderItem {self.id} Of {self.order} Order"
    

