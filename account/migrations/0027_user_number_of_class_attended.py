# Generated by Django 3.2.9 on 2021-11-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_session_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number_of_class_attended',
            field=models.IntegerField(default=0),
        ),
    ]
