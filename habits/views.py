from rest_framework import generics

from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateView(generics.CreateAPIView):
    """Контроллер создания привычки"""
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        """Привязываем текущего пользователя к создаваемому объекту"""
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitDetailView(generics.RetrieveAPIView):
    """Контроллер просмотра привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateView(generics.UpdateAPIView):
    """Контроллер редактирования привычки"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDeleteView(generics.DestroyAPIView):
    """Контроллер удаления привычки"""
    queryset = Habit.objects.all()


class HabitListView(generics.ListAPIView):
    """Контроллер просмотра списка привычек"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
