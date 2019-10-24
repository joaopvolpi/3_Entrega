from django.urls import path 
from rest_framework.routers import DefaultRouter
from api.views import PostagemViewSet, UserCreate, LoginView, ComentarioViewSet

router = DefaultRouter()
router.register('postagem', PostagemViewSet, base_name='postagem')
router.register('comentario', ComentarioViewSet, base_name='comentario')

urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
]
urlpatterns+=router.urls



