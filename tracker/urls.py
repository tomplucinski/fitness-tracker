from django.urls import path
from . import views


urlpatterns = [
    path('workouts', views.create_workout, name='create_workout'),
]
