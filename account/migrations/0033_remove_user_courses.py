# Generated by Django 3.2.9 on 2021-11-27 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0032_remove_course_course_streak'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='courses',
        ),
    ]
