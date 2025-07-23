from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile

# Enregistre le modèle User personnalisé
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass  # Tu peux personnaliser l'interface d'admin ici si besoin

# Enregistre le modèle Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email')
