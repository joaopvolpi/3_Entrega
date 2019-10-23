#PASSAR DE PYTHON PARA JSON

from rest_framework import serializers
from api.model.Postagem import Postagem

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'