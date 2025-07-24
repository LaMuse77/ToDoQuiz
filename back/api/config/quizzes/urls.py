# quiz/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet , QuestionCreateViewSet

router = DefaultRouter()
router.register('quizzes', QuizViewSet)
router.register('questions', QuestionCreateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
