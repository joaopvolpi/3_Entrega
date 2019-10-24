from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from api.model.Postagem import Postagem


class Comentario(models.Model):

    created_by =  models.ForeignKey(User,on_delete=models.CASCADE) #Liga o comentario ao usuario
    post = models.ForeignKey(Postagem,on_delete=models.CASCADE) #Liga o comentario à postagem
    descricao = models.TextField()
    data_criada = models.DateTimeField(default=timezone.now)

def __str__(self):
    return self.nome
