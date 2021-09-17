from django.db import models
from django.conf import settings
from contas.models import Usuario
from django.template.defaultfilters import slugify
from django.utils import timezone as tz

# Create your models here.


class Noticia(models.Model):
    """Entidade de Notícias do Banco de Dados"""
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL, null=True)
    texto = models.TextField()
    criacao = models.DateTimeField(auto_now_add=True)
    edicao = models.DateTimeField(default=tz.now, blank=True, null=True)
    ESCOLHAS_CATEGORIA = (
        ('comunicados', 'Comunicados'),
        ('equipamentos', 'Equipamentos'),
        ('compras', 'Compras'),
        ('manutencao', 'Manutenção'),
        ('treinamentos', 'Treinamentos'),
        ('pesquisa', 'Pesquisa'),
    )
    categoria = models.CharField(
        max_length=15, choices=ESCOLHAS_CATEGORIA, default='comunicados')
    status = models.BooleanField(default=False)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Noticia, self).save(*args, **kwargs)
