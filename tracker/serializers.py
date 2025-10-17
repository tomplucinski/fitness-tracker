from rest_framework import serializers
from .models import Workout, Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'workout', 'name', 'sets', 'reps', 'weight']

    def validate_workout(self, value):
        if not value:
            raise serializers.ValidationError("Workout ID is required.")
        return value


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)
    class Meta:
        model = Workout
        fields = ['id', 'user', 'name', 'date_created', 'exercises']
