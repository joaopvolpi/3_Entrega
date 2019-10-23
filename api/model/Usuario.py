from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    senha = models.CharField(max_length=30)
    bio = models.TextField()
    #foto_perfil = models.ImageField()

def __str__(self):
    return self.username 

