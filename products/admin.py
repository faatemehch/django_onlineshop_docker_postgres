from django.contrib import admin
from .models import Product, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ('author',
              'text',
              'points',
              'active',)
    extra = 0 # To remove empty records


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'active')
    inlines = (CommentsInline, )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'active', 'datetime_created')
