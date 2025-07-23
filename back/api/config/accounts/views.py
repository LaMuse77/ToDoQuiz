from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from accounts.models import Profile

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)

            # 🔥 Ajoute ceci pour inclure le rôle dans la réponse :
            try:
                profile = Profile.objects.get(user=user)
                role = profile.role
            except Profile.DoesNotExist:
                role = None

            return Response({
                "token": token.key,
                "role": role,
            })

        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
