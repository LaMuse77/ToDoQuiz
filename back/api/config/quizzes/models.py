from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Quiz(models.Model):   
    titre = models.CharField(max_length=255)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='quizzes')  # Added missing field

    def __str__(self):
        return self.titre 

class Question(models.Model):
    texte = models.TextField()
    type = models.CharField(max_length=20, choices=[('text', 'Texte'), ('image', 'Image')])
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Choice(models.Model):
    texte = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='choices/', blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choix = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    texte_libre = models.TextField(blank=True)

    def __str__(self):
        return f"Réponse de {self.user} à {self.question}"
