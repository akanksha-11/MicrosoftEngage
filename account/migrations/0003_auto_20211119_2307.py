# Generated by Django 3.0.7 on 2021-11-19 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20211119_2216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='course',
            new_name='courses',
        ),
    ]
