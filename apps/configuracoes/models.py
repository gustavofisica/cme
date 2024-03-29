from django.db import models

# Create your models here.
class Configuracoes(models.Model):
    """Entidade de configurações"""
    noticias_index = models.PositiveSmallIntegerField(unique=True, default=5)
    tecnicas = models.JSONField(default=dict, null=True, blank=True)
