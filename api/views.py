#pip3 install django
#pip3 install djangorestframework

#building APIs with Django

from django.shortcuts import render
from rest_framework.response import Response #Manda resposta em JSON
from rest_framework.views import APIView 
from api.model.Postagem import Postagem
from api.model.Usuario import Usuario
from .serializers import PostagemSerializer, UserSerializer
from rest_framework import generics, status, viewsets
from django.contrib.auth import authenticate


class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
        permission_classes = ()
        def post(self, request):
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                return Response({"token": user.auth_token.key})
            else:
                return Response({"error": "Senha Incorreta"}, status=status.HTTP_400_BAD_REQUEST)  