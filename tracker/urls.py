from django.urls import path
from . import views


urlpatterns = [
    path('workouts', views.create_workout, name='create_workout'),
    path('exercises', views.get_exercises, name='get_exercises'),
    path('users/<int:user_id>/exercises', views.get_user_exercises, name='get_user_exercises')
]
