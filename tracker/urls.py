from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.hello_world),
    path('workouts/', views.create_workout, name='create_workout'),
]