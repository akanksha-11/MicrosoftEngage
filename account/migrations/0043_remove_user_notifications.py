# Generated by Django 3.2.9 on 2021-11-27 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0042_user_notifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Notifications',
        ),
    ]
