# Generated by Django 5.0.3 on 2024-03-11 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_habit_start_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='duration',
            field=models.DurationField(default='00:00', verbose_name='Выполнять мм:сс'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='start_point',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 11, 18, 22, 0, 304358, tzinfo=datetime.timezone.utc), verbose_name='Когда?'),
        ),
    ]
