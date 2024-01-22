from django.db import models


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
