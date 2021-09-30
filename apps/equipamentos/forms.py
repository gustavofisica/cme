from django import forms
from django.forms import fields
from equipamentos.models import Equipamento, GeleriaEquipamento


class FormularioEquipamento(forms.ModelForm):

    class Meta:
        model = Equipamento
        fields = '__all__'


class FormularioGeleriaEquipamento(forms.ModelForm):

    class Meta:
        model = GeleriaEquipamento
        fields = '__all__'


class FormularioTecnicas(forms.Form):
    imagem_eletron_secundarios = forms.BooleanField()
    imagem_eletron_retroespalhados = forms.BooleanField()
    imagem_eletron_transmitidos_campo_claro = forms.BooleanField()
    imagem_eletron_transmitidos_campo_escuro = forms.BooleanField()
    controle_de_temperatura = forms.BooleanField()
    SAED = forms.BooleanField()
    EDS = forms.BooleanField()
    WDS = forms.BooleanField()
