from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetiem_created = models.DateTimeField(auto_now_add=True)
    datetiem_modified = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=1)
    # image = models.ImageField()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    CHOICES = (
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetiem_modified = models.DateTimeField(auto_now=True)
    points = models.CharField(choices=CHOICES)
    active = models.BooleanField(default=True)

    # Manager
    objects = models.Manager()
    active_commnets_manager = ActiveCommentsManager()

    def __str__(self):
        return str(self.product)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.product.id})
