# Generated by Django 2.2.4 on 2020-06-02 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0025_auto_20200602_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('product_image', models.CharField(max_length=100)),
                ('is_ordered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=200)),
                ('is_addressed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField(default='')),
                ('number', models.CharField(max_length=15)),
                ('pincode', models.PositiveIntegerField(default=0)),
                ('GST_number', models.PositiveIntegerField(default=0)),
                ('Bank_Account_Details', models.TextField(default='')),
                ('store_name', models.CharField(max_length=50)),
                ('store_description', models.CharField(max_length=200)),
                ('store_address', models.TextField(default='')),
                ('is_approved', models.BooleanField(default=False)),
                ('supplier_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pr', models.CharField(choices=[('S', 'Supplier'), ('C', 'Customer'), ('A', 'Admin')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('product_price', models.IntegerField(default=0)),
                ('out_of_stock', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=100)),
                ('product_image', models.CharField(max_length=100)),
                ('product_sku', models.IntegerField(default=1)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('referral_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('state', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('apartmentno', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=6)),
                ('is_completed', models.BooleanField(default=False)),
                ('total_amount', models.IntegerField(default=0)),
                ('is_refunded', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='shop.Cart')),
                ('supplier', models.ManyToManyField(to='shop.Supplier')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('apartmentno', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=6)),
                ('category', models.CharField(choices=[('1', 'Category1'), ('2', 'Category2')], max_length=1)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
