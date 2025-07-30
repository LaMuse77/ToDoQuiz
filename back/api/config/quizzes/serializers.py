# quiz/serializers.py
from rest_framework import serializers
from .models import Quiz, Question, Choice



# back/api/config/quizzes/serializers.py
from rest_framework import serializers
from .models import Quiz, Question, Choice, Categorie

class CategorieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ['id', 'nom']

class ChoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['texte', 'image']

    def validate(self, data):
        if not data.get('texte') and not data.get('image'):
            raise serializers.ValidationError("Un choix doit avoir un texte ou une image.")
        return data

class QuestionCreateSerializer(serializers.ModelSerializer):
    choices = ChoiceCreateSerializer(many=True)

    class Meta:
        model = Question
        fields = ['texte', 'type', 'choices', 'quiz']

    def validate(self, data):
        if not data.get('choices'):
            raise serializers.ValidationError("Une question doit avoir au moins un choix.")
        return data

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question

class QuizCreateSerializer(serializers.ModelSerializer):
    questions = QuestionCreateSerializer(many=True, write_only=True)
    categorie = serializers.PrimaryKeyRelatedField(queryset=Categorie.objects.all())

    class Meta:
        model = Quiz
        fields = ['titre', 'description', 'categorie', 'questions']

    def validate(self, data):
        if not data.get('questions'):
            raise serializers.ValidationError("Un quiz doit avoir au moins une question.")
        return data

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data)
        for q_data in questions_data:
            choices_data = q_data.pop('choices', [])
            question = Question.objects.create(quiz=quiz, **q_data)
            for choice_data in choices_data:
                Choice.objects.create(question=question, **choice_data)
        return quiz