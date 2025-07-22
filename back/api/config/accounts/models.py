from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass  # Tu peux ajouter des champs ici si besoin plus tard

class Profile(models.Model):
    ROLE_CHOICES = (
        ('organisateur', 'Organisateur'),
        ('participant', 'Participant'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
