from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Configuracoes
from contas.models import Usuario

def nova_tecnica(request, username):

    usuario = get_object_or_404(Usuario, username=username)

    if request.method == 'POST':

        configuracoes = Configuracoes.objects.last()

        tecnicas = configuracoes.tecnicas

        ultima_tecnica_registrada = list(tecnicas.keys())[-1]

        separador = ultima_tecnica_registrada.find("_")

        chave_proxima_tecnica = f'tecnica_{int(ultima_tecnica_registrada[(separador + 1):]) + 1}'

        nova_tecnica = request.POST['nova_tecnica']

        tecnicas[chave_proxima_tecnica] = nova_tecnica

        configuracoes.save()

        return redirect(reverse('cria_equipamento', args=[usuario.username]))
