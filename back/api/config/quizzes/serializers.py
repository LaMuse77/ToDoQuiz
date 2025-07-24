# quiz/serializers.py
from rest_framework import serializers
from .models import Quiz, Question, Choice

# quizzes/serializers.py
from rest_framework import serializers
from .models import Quiz, Question, Choice, Categorie

class CategorieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice 
        fields = ['nom']
    

class ChoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['texte', 'image']

class QuestionCreateSerializer(serializers.ModelSerializer):
    choices = ChoiceCreateSerializer(many=True)

    class Meta:
        model = Question
        fields = ['texte', 'type', 'choices', 'quiz']

    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            image = choice_data.get('image')
            if image:
                Choice.objects.create(question=question, image=image, **choice_data)
            else:
                Choice.objects.create(question=question, **choice_data)
        return question

class QuizCreateSerializer(serializers.ModelSerializer):
    questions = QuestionCreateSerializer(many=True, write_only=True)
    categorie = serializers.PrimaryKeyRelatedField(queryset=Categorie.objects.all())

    class Meta:
        model = Quiz
        fields = ['titre', 'description', 'categorie', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data)
        for q_data in questions_data:
            choices_data = q_data.pop('choices', [])
            question = Question.objects.create(quiz=quiz, **q_data)
            for choice_data in choices_data:
                image = choice_data.get('image')
                if image:
                    Choice.objects.create(question=question, image=image, **choice_data)
                else:
                    Choice.objects.create(question=question, **choice_data)
        return quiz