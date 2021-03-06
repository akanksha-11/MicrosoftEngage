# Generated by Django 3.0.7 on 2021-11-20 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20211120_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[(1, 'Student'), (2, 'Teacher')], default=1, max_length=10),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('session_day', models.CharField(max_length=255)),
                ('session_start_time', models.DateTimeField()),
                ('session_end_time', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Course')),
            ],
        ),
    ]
