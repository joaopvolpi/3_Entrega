from django.urls import path
from api.views import PostagemList

urlpatterns = [
    path('postagem/',PostagemList.as_view())
]