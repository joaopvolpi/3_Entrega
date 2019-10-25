from django.db import models
from django.contrib.auth.models import User
from api.model.Postagem import Postagem


class Curtida(models.Model):

    created_by =  models.ForeignKey(User,on_delete=models.CASCADE)
    post =  models.ForeignKey(Postagem,on_delete=models.CASCADE)
    
    

