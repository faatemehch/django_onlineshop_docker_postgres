from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('product title'))
    short_description = models.CharField(_("Short Description"), max_length=300, blank=True)
    description = RichTextField()
    datetime_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created date'))
    datetime_modified = models.DateTimeField(
        auto_now=True, verbose_name=_('last modified date'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('price'))
    active = models.BooleanField(default=1, verbose_name=_('Active\Inactive'))
    image = models.ImageField(verbose_name=_("Product Image"), upload_to='product/product_image', blank=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    CHOICES = (
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='comments', verbose_name=_('product'))
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='comments', verbose_name=_('author text'))
    text = models.TextField(verbose_name=_('message text'))
    datetime_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created date'))
    datetiem_modified = models.DateTimeField(
        auto_now=True, verbose_name=_('modified date'))
    points = models.CharField(choices=CHOICES, verbose_name=_('Points'))
    active = models.BooleanField(
        default=True, verbose_name=_('Active \ Inactive'))
    
    # Manager
    objects = models.Manager()
    active_commnets_manager = ActiveCommentsManager()
    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.product.id})
