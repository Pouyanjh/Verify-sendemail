# Generated by Django 4.1.7 on 2023-03-30 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_user_is_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
    ]
