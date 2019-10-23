from django.db import models
from django.utils import timezone
from api.model.Usuario import Usuario



class Postagem(models.Model):

    #autor =  models.ForeignKey(Usuario,on_delete=models.CASCADE)
    nome = models.TextField()
    descricao = models.TextField()
    data_criada = models.DateTimeField(default=timezone.now)
    #imagem = models.ImageField()
    

def __str__(self):
    return self.nome
