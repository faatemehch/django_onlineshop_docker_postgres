# Generated by Django 4.2.9 on 2024-02-05 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Order Item', 'verbose_name_plural': 'OrderItems'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='phone_numbe',
            new_name='phone_number',
        ),
    ]
