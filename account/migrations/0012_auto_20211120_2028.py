# Generated by Django 3.0.7 on 2021-11-20 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20211120_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='course_id',
            new_name='course',
        ),
    ]
