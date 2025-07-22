from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User
from quizzes.models import Quiz, Question, Choice

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    date_soumission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.titre}"

class Response(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choix = models.ForeignKey(Choice, on_delete=models.SET_NULL, null=True, blank=True)
    texte_libre = models.TextField(blank=True)

    def __str__(self):
        return f"Réponse à {self.question} dans {self.submission}"
