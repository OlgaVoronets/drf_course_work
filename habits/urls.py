from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListView, HabitCreateView, HabitDetailView, HabitUpdateView, HabitDeleteView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/', HabitListView.as_view(), name='habit_list'),
    path('habit/create/', HabitCreateView.as_view(), name='habit_create'),
    path('habit/<int:pk>/', HabitDetailView.as_view(), name='habit_view'),
    path('habit/update/<int:pk>/', HabitUpdateView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDeleteView.as_view(), name='habit_delete'),
]
