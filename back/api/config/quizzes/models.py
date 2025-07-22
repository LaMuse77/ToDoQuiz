from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Quiz(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titre

class Question(models.Model):
    TYPE_CHOICES = (
        ('choix_multiple', 'Choix Multiple'),
        ('texte_libre', 'Texte Libre'),
    )
    texte = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.texte

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    texte = models.CharField(max_length=255)

    def __str__(self):
        return self.texte

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choix = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    texte_libre = models.TextField(blank=True)

    def __str__(self):
        return f"Réponse de {self.user} à {self.question}"
