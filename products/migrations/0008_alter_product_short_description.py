# Generated by Django 4.2.9 on 2024-02-04 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_short_description_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=300, verbose_name='Short Description'),
        ),
    ]
