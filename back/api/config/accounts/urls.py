from django.urls import path
from .views import RegisterView, LoginView
#from django.apps import rest_framework 
from rest_framework_simplejwt.views import TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
   # path('api/token/', csrf_exempt(TokenObtainPairView.as_view()), name='token_obtain_pair'),
]
