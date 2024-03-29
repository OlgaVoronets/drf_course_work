# Generated by Django 5.0.3 on 2024-03-11 18:53

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_habit_duration_alter_habit_start_point'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='duration',
            field=models.DurationField(default='00:00', verbose_name='Выполнять чч:мм:сс'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='start_point',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 11, 18, 53, 0, 189077, tzinfo=datetime.timezone.utc), verbose_name='Когда?'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель привычки'),
        ),
    ]
