from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Workout
from .serializers import WorkoutSerializer
from django.contrib.auth.models import User
from .services.workout_service import WorkoutService


@api_view(['POST'])
def create_workout(request):
    """Create a new workout."""
    serializer = WorkoutSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    workout = WorkoutService.create_workout(serializer.validated_data)
    return Response(WorkoutSerializer(workout).data, status=status.HTTP_201_CREATED)