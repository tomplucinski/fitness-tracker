from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import WorkoutSerializer


#need error handling
@api_view(['POST'])
def create_workout(request):
    """Create a new workout."""
    serializer = WorkoutSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    workout = serializer.save()
    return Response(WorkoutSerializer(workout).data, status=status.HTTP_201_CREATED)
    