from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/dashboard/noticias/', views.noticias, name='noticias'),
    # CRUD Notícias
    path('<str:username>/dashboard/nova_noticia', views.nova_noticia, name='nova_noticia'),
    path('<str:username>/dashboard/editar_noticia/<slug:slug>', views.editar_noticia, name='editar_noticia'),
    path('<str:username>/dashboard/deletar_noticia/<slug:slug>', views.deletar_noticia, name='deletar_noticia'),
]