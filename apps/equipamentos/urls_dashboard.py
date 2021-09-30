from django.urls import path
from . import views

urlpatterns = [
    # URLs do Dashboard
    path('<str:username>/dashboard/listar_equipamentos/', views.listar_equipamentos, name='listar_equipamentos'),
    # CRUD Notícias
    path('<str:username>/dashboard/novo_equipamento/', views.novo_equipamento, name='novo_equipamento'),
    path('<str:username>/dashboard/editar_equipamento/<int:id_equipamento>', views.editar_equipamento, name='editar_equipamento'),
    path('<str:username>/dashboard/deletar_equipamento/<int:id_equipamento>', views.deletar_equipamento, name='deletar_equipamento'),
]