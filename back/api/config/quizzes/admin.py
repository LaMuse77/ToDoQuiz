from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categorie, Quiz, Question, Choice, Answer

admin.site.register(Categorie)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Answer)