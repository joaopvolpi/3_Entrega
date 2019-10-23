from django.urls import path
from api.views import PostagemList, UsuarioList

urlpatterns = [
    path('postagem/',PostagemList.as_view()),
    path('users/',UsuarioList.as_view()),#PARA CRIAR O USUARIO
]