# Generated by Django 5.0.1 on 2024-02-12 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0030_alter_shippingdetails_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingdetails',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_details', to='crm.product'),
        ),
    ]