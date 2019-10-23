#pip3 install django
#pip3 install djangorestframework

#building APIs with Django

from django.shortcuts import render
from rest_framework.response import Response #Manda resposta em JSON
from rest_framework.views import APIView 
from api.model.Postagem import Postagem
from api.model.Usuario import Usuario
from api.serializers import PostagemSerializer, UserSerializer

# Create your views here.

class PostagemList(APIView):
    def get(self, request):
        postagem=Postagem.objects.all()
        data = PostagemSerializer(postagem, many=True).data
        postagem.save()

    def post(self, request):
        #autor = request.data['autor']
        nome = request.data['nome']
        descricao = request.data['descricao']
        postagem = Postagem(autor=nome,descricao=descricao)
        postagem.save()
        data = PostagemSerializer(postagem).data
        
        return Response(data)

   # def put(self):
    #    pass
   # def post(self):
    #    pass

class UsuarioList(APIView):
    def get(self, request):
        usuario=usuario.objects.all()
        data = UsuarioSerializer(postagem, many=True).data
        usuario.save()

    def post(self, request):
        username = request.data['username']
        senha = request.data['senha']
        nome = request.data['nome']
        bio = request.data['bio']
        postagem = Postagem(username=username,senha=senha,nome=nome,bio=bio)
        postagem.save()
        data = PostagemSerializer(postagem).data
        
        return Response(data)

  #  def put(self):
   #     pass
    #def post(self):
     #   pass



