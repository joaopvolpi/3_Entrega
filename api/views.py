#pip3 install django
#pip3 install djangorestframework

#building APIs with Django

from django.shortcuts import render
from rest_framework.response import Response #Manda resposta em JSON
from rest_framework.views import APIView 
from api.model.Postagem import Postagem
from api.model.Comentario import Comentario
#from api.model.Usuario import Usuario
from .serializers import PostagemSerializer, UserSerializer, ComentarioSerializer
from rest_framework import generics, status, viewsets
from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied


class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    
    def destroy(self, request, *args, **kwargs):
        postagem = Postagem.objects.get(pk=self.kwargs["pk"])
        if not request.user == postagem.created_by:
            raise PermissionDenied("Você não pode deletar essa postagem")
            return super().destroy(request, *args, **kwargs)


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    
    def destroy(self, request, *args, **kwargs):
        comentario = Comentario.objects.get(pk=self.kwargs["pk"])
        if not request.user == comentario.created_by:
            raise PermissionDenied("Você não pode deletar esse comentario")
            return super().destroy(request, *args, **kwargs)


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
                return Response({"token": user.auth_token.key}) #RETORNA UM TOKEN PRO USUARIO QUE ACERTAR USERNAME E SENHA
            else:
                return Response({"error": "Senha Incorreta"}, status=status.HTTP_400_BAD_REQUEST)  