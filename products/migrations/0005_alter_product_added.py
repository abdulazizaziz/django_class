# Generated by Django 4.1.7 on 2023-07-10 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='added',
            field=models.DateField(auto_now_add=True),
        ),
    ]