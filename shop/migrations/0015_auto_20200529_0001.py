# Generated by Django 2.2.4 on 2020-05-28 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='order',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
    ]