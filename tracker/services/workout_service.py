from ..models import Workout, Exercise, WorkoutLog

class WorkoutService:
    @staticmethod
    def create_workout(data):
        return Workout.objects.create(**data)
    