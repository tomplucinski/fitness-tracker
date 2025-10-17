from rest_framework import viewsets

from ..models import Exercise, Workout
from ..serializers import ExerciseSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        """
        If nested route is used (/workouts/{id}/exercises/),
        filter by that workout.
        Otherwise return all exercises.
        """
        workout_id = self.kwargs.get('workout_pk')
        if workout_id:
            return Exercise.objects.filter(workout_id=workout_id)
        return Exercise.objects.all()
    
    def perform_create(self, serializer):
        """
        Automatically link the exercise to the workout
        when using the nested route.
        """
        workout_id = self.kwargs.get('workout_pk')
        if workout_id:
            workout = Workout.objects.get(pk=workout_id)
            serializer.save(workout=workout)
        else:
            serializer.save()
