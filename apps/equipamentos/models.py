from django.db import models
import os.path
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from cme.settings import THUMB_SIZE

from PIL import Image


class Equipamento(models.Model):
    nome_do_equipamento = models.CharField(max_length=255)
    apelido = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    url_fabricante = models.URLField(null=True)
    descricao = models.TextField(null=True, blank=True)
    numero_patrimonio = models.IntegerField(null=True, blank=True)
    ESCOLHAS_TIPO_DE_EQUIPAMENTO = (
        ('SEM', 'Microscópio Eletrônico de Varredura'),
        ('TEM', 'Microscópio Eletrônico de Transmissão'),
        ('Raman', 'Microscópio Confocal Raman'),
        ('AFM', 'Microscópio de Força Atômica'),
        ('Preparo', 'Preparo de Amostra'),
    )
    tipo_de_equipamento = models.CharField(
        max_length=15, choices=ESCOLHAS_TIPO_DE_EQUIPAMENTO,)
    microscopio = models.BooleanField(default=False)
    pre_microscopia = models.BooleanField(default=False)
    sala = models.CharField(max_length=255, null=True, blank=True)
    tecnicas = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return self.nome_do_equipamento


def nomear_pasta(instancia, nome_do_arquivo):
    return f'{instancia.equipamento.apelido}/{nome_do_arquivo}'


class GeleriaEquipamento(models.Model):
    imagem = models.ImageField(upload_to=nomear_pasta)
    equipamento = models.ForeignKey(
        Equipamento, on_delete=models.CASCADE, related_name='imagens')
    descricao_da_imagem = models.CharField(max_length=500)
    foto_de_perfil = models.BooleanField(default=False)
    miniatura = models.ImageField(upload_to=nomear_pasta, editable=False)

    def save(self, *args, **kwargs):

        if not self.cria_miniatura():
            # set to a default miniatura
            raise Exception(
                'Não foi possível criar a miniatura - o arquivo é válido?')

        super(GeleriaEquipamento, self).save(*args, **kwargs)

    def cria_miniatura(self):

        image = Image.open(self.imagem)
        image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.imagem.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False    # Unrecognized file type

        # Save miniatura to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.miniatura.save(thumb_filename, ContentFile(
            temp_thumb.read()), save=False)
        temp_thumb.close()

        return True


class AcessorioEquipamento(models.Model):
    nome_do_acessorio = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    descricao = models.TextField()
    numero_patrimonio = models.IntegerField()
    equipamento = models.ForeignKey(
        Equipamento, on_delete=models.CASCADE, related_name='acessorios')
