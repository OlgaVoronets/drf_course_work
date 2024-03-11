from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Habit(models.Model):
    """Модель привычки:
    Поле related_habit указывается только для полезной привычки
    Поле is_nice - признак приятной привычки, можно привязать к полезной
    Поле reward указывается только для полезной привычки, если нет привязки к приятной
    """

    PERIOD_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('in 2 days', 'каждые 2 дня'),
        ('in 3 days', 'каждые 3 дня'),
        ('in 4 days', 'каждые 4 дня'),
        ('in 5 days', 'каждые 5 дней'),
        ('in 6 days', 'каждые 6 дней'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Cоздатель привычки',
                             related_name='user')

    action = models.TextField(verbose_name='Что?')
    place = models.CharField(max_length=150, verbose_name='Где?')
    time = models.TimeField(verbose_name='Когда?')
    duration = models.DurationField(verbose_name='Как долго?')
    period = models.CharField(max_length=20, verbose_name='Как часто?', choices=PERIOD_CHOICES, default='daily')

    is_nice = models.BooleanField(default=False, verbose_name='Приятная')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')

    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE,
                                      verbose_name='Связанная привычка', related_name='good_habit')
    reward = models.TextField(**NULLABLE, verbose_name='Вознаграждение')

    def __str__(self):
        return f'{self.period} {self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

