# Generated by Django 3.2.9 on 2021-11-23 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_user_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='\\static'),
        ),
    ]
