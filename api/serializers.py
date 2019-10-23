#PASSAR DE PYTHON PARA JSON

from rest_framework import serializers
from api.model.Postagem import Postagem
from api.model.Usuario import Usuario
from django.contrib.auth.models import User

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:        #SERA QUE DA RUIM?
        model = User
        fields = {'username','password', 'email'}
        extra_kwargs = {'password':{'write-only':True}}
    
    def create(self,validated_data):
        user = User(
            email=validated_data['email'],
            username =validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user