# Generated by Django 4.1.7 on 2023-03-17 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, max_length=100),
        ),
    ]