from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Workout
from .serializers import WorkoutSerializer
from django.contrib.auth.models import User


# Create your views here.

def hello_world(request):
    return JsonResponse({"message": "Hello, world!"})

@api_view(['POST'])
def create_workout(request):
    """Create a new workout."""
    serializer = WorkoutSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)