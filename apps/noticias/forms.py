from noticias.models import Noticia
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from tempus_dominus.widgets import DateTimePicker


class FormularioNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'
        exclude = ['slug', 'autor']
        labels = {
            'titulo': 'Título da Notícia',
            'texto': 'Texto',
            'criacao': 'Data de Criação',
            'edicao': 'Data de Edição',
            'status': 'Marque para publicar',
            'destaque': 'Destacar notícia',
            'categoria': 'Categoria',
        }
        widgets = {
            'criacao': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
            'edicao': DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
            'texto': SummernoteWidget(),
        }
