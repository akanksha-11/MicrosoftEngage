# Generated by Django 3.2.9 on 2021-11-27 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0038_remove_session_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='uploaded',
            field=models.IntegerField(default=0),
        ),
    ]
