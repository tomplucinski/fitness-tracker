from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import WorkoutSerializer, ExerciseSerializer
from .models import Exercise

#need error handling
@api_view(['POST'])
def create_workout(request):
    """Create a new workout."""
    serializer = WorkoutSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    workout = serializer.save()
    return Response(WorkoutSerializer(workout).data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def get_exercises(request):
    """Get all exercises"""
    exercises = Exercise.objects.all()
    serializer = ExerciseSerializer(exercises, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_exercises(request, user_id=None):
    """Get all exercises for user"""
    if user_id is None:
        return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    exercises = Exercise.objects.filter(workout__user_id=user_id)
    serializer = ExerciseSerializer(exercises, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
