# Generated by Django 3.2.9 on 2021-11-26 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_auto_20211127_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
