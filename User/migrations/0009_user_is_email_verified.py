# Generated by Django 4.1.7 on 2023-03-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_user_activation_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]