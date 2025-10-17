from rest_framework_nested import routers

from tracker.views.exercise_views import ExerciseViewSet
from tracker.views.workout_views import WorkoutViewSet

# Base router
router = routers.DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workout')

# Nested router
workout_router = routers.NestedDefaultRouter(router, r'workouts', lookup='workout')
workout_router.register(r'exercises', ExerciseViewSet, basename='workout-exercises')

urlpatterns = router.urls + workout_router.urls
