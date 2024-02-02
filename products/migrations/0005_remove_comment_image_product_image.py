# Generated by Django 4.2.9 on 2024-02-02 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_comment_image_alter_comment_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/product_image', verbose_name='Product Image'),
        ),
    ]