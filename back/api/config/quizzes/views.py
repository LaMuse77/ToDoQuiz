from django.shortcuts import render

# Create your views here.


# quizzes/views.py
from rest_framework import viewsets , mixins
from .models import Question, Quiz , Categorie
from .serializers import QuestionCreateSerializer, QuizCreateSerializer , CategorieCreateSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly , AllowAny
from rest_framework.parsers import MultiPartParser, FormParser


class QuestionCreateViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]

    def get_serializer_context(self):
        return {'request': self.request}
    

class CategorieViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]