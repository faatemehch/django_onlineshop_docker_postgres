# Generated by Django 4.2.9 on 2024-02-02 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_comment_image_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='datetiem_created',
            new_name='datetime_created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='datetiem_modified',
            new_name='datetime_modified',
        ),
    ]