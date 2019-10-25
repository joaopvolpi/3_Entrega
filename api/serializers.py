#PASSAR DE PYTHON PARA JSON

from rest_framework import serializers
from api.model.Postagem import Postagem
from api.model.Comentario import Comentario
from api.model.Curtida import Curtida
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'
        

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'

class CurtidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curtida
        fields = '__all__'