from django.shortcuts import render

# Create your views here.


# quizzes/views.py
from rest_framework import viewsets , mixins
from .models import Question, Quiz , Categorie
from .serializers import * 
from rest_framework.permissions import IsAuthenticatedOrReadOnly , AllowAny
from rest_framework.parsers import MultiPartParser, FormParser


from django.shortcuts import render

# Create your views here.


# quizzes/views.py
from rest_framework import viewsets , mixins
from .models import Question, Quiz , Categorie
from .serializers import * 
from rest_framework.permissions import IsAuthenticatedOrReadOnly , AllowAny
from rest_framework.parsers import MultiPartParser, FormParser


# back/api/config/quizzes/views.py
from rest_framework import viewsets, mixins
from .models import Question, Quiz, Categorie
from .serializers import QuestionCreateSerializer, QuizCreateSerializer, CategorieCreateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

class QuestionCreateViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer
    permission_classes = [IsAuthenticated]

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']  # Explicitly allow POST

    def get_serializer_context(self):
        return {'request': self.request}

class CategorieViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieCreateSerializer
    permission_classes = [AllowAny]