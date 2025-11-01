from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create your views here.
@api_view(['GET'])
def Home(request):
    return Response("Hello world")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ProtectedView(request):
    return Response(f"Hello, {request.user.username}. this user is authenticated.")


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
