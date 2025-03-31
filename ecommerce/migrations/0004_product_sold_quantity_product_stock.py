# Generated by Django 5.1.6 on 2025-03-31 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_featuredproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
