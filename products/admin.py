from django.contrib import admin
from .models import Product, Comment
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from django.utils.translation import gettext_lazy as _

class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ('author',
              'text',
              'points',
              'active',)
    extra = 0 # To remove empty records


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('__str__', 'active', 'get_created_jalali')
    inlines = (CommentsInline, )

    @admin.display(description=_('DateTime Created'), ordering='datetime_created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.datetime_created).strftime('%B %Y - %H:%M')


@admin.register(Comment)
class CommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('__str__', 'author', 'active', 'get_created_jalali')


    @admin.display(description=_('DateTime Created'), ordering='datetime_created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.datetime_created).strftime('%a, %d %b %Y %H:%M:%S')
