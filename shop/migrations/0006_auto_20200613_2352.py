# Generated by Django 2.2.4 on 2020-06-13 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200613_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='society',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Society'),
        ),
    ]