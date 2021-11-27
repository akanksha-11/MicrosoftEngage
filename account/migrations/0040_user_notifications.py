# Generated by Django 3.2.9 on 2021-11-27 21:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0039_session_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Notifications',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20, null=True), default='Welcome', size=6),
            preserve_default=False,
        ),
    ]
