#pip3 install django
#pip3 install djangorestframework

#building APIs with Django

from django.shortcuts import render
from rest_framework.response import Response #Manda resposta em JSON
from rest_framework.views import APIView 
from api.model.Postagem import Postagem
from api.serializers import PostagemSerializer

# Create your views here.

class PostagemList(APIView):
    def get(self, request):
        postagem=Postagem.objects.all()
        data = PostagemSerializer(postagem, many=True).data
        postagem.save()

    def post(self, request):
        nome = request.data['nome']
        descricao = request.data['descricao']
        postagem = Postagem(nome=nome,descricao=descricao)
        postagem.save()
        data = PostagemSerializer(postagem).data
        
        return Response(data)

    def put(self):
        pass
    def post(self):
        pass

