# Generated by Django 5.0.1 on 2024-01-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_profile_aadhar_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='aadhar_card',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
