from django import forms
from django.forms import fields
from .models import Configuracoes


class FormularioNovaTecnica(forms.ModelForm):

    class Meta:
        model = Configuracoes
        fields = ['tecnicas']