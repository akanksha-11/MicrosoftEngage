# Generated by Django 3.2.9 on 2021-11-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_session_lecture_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='attendance_percentage',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
