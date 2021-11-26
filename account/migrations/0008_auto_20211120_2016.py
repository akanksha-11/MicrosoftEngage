# Generated by Django 3.0.7 on 2021-11-20 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_session_session_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='account.Course'),
        ),
    ]
