# Generated by Django 3.2.9 on 2021-11-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_alter_session_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_streak',
            field=models.IntegerField(default=0),
        ),
    ]
