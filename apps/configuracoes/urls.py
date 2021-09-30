from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/nova_tecnica/', views.nova_tecnica, name='nova_tecnica')
]
