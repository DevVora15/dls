# Generated by Django 5.0.1 on 2024-02-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0037_alter_product_highest_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingdetails',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='highest_bid',
            field=models.IntegerField(default=0),
        ),
    ]