# Generated by Django 3.2.9 on 2021-11-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20211122_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
