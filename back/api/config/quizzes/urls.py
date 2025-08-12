# quiz/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet , QuestionCreateViewSet, CategorieViewSet


router = DefaultRouter()
router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'questions', QuestionCreateViewSet, basename='question')
router.register(r'categories', CategorieViewSet, basename='categorie')

urlpatterns = [
    path('api/', include(router.urls)),
]   
    