from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели привычки"""

    class Meta:
        model = Habit
        fields = '__all__'
