# Generated by Django 5.0.1 on 2024-02-01 16:14

import django.db.models.deletion
import shortuuid.django_fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0013_alter_profile_aadhar_card'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='cat', unique=True)),
                ('title', models.CharField(default='Items', max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='category_pics')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='', unique=True)),
                ('product_name', models.CharField(default='Items', max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='product_pics')),
                ('description', models.TextField(blank=True, default='This is the product', null=True)),
                ('min_price', models.DecimalField(decimal_places=2, default='2000', max_digits=99999999999)),
                ('price_interval', models.DecimalField(decimal_places=2, default='100', max_digits=99999999999)),
                ('date', models.DateField(auto_now_add=True)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='crm.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='sel', unique=True)),
                ('title', models.CharField(default='', max_length=100)),
                ('description', models.TextField(blank=True, default='I am an Ama=azing Seller', null=True)),
                ('address', models.CharField(default='123 Main Street London', max_length=100)),
                ('contact', models.CharField(default='+91 (1234) 567890', max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sellers',
            },
        ),
    ]