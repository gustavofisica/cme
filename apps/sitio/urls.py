from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('normas', views.normas, name='normas'),
    path('contato', views.contato, name='contato'),
]