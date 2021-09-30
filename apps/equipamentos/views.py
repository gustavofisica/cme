from typing import Mapping
from django.urls import reverse
from equipamentos.forms import FormularioEquipamento, FormularioGeleriaEquipamento, FormularioTecnicas
from equipamentos.models import Equipamento, GeleriaEquipamento, AcessorioEquipamento
from contas.models import Usuario
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from configuracoes.models import Configuracoes
from configuracoes.forms import FormularioNovaTecnica
from django.db.models.query_utils import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def equipamentos(request):
    """Rederiza os equipamentos de microscopia"""
    equipamentos = Equipamento.objects.all()

    dados = {
        'equipamentos': equipamentos,
    }

    return render(request, 'equipamentos/equipamentos.html', dados)


@login_required
def listar_equipamentos(request, username):

    usuario = get_object_or_404(Usuario, username=username)

    equipamentos = Equipamento.objects.all()

    if request.method == 'POST':

        equipamentos = Equipamento.objects.filter(
            Q(nome_do_equipamento__icontains=request.POST['table_search']) |
            Q(descricao__icontains=request.POST['table_search']) |
            Q(tipo_de_equipamento__icontains=request.POST['table_search'])
        )

    numero_de_equipamentos_renderizadas = 5

    paginator = Paginator(equipamentos, numero_de_equipamentos_renderizadas)

    page = request.GET.get('page')

    equipamentos_por_pagina = paginator.get_page(page)

    dados = {
        'usuario': usuario,
        'equipamentos': equipamentos_por_pagina,
    }

    return render(request, 'admin/dashboard/equipamentos/lista_equipamentos.html', dados)


@login_required
def novo_equipamento(request, username):

    usuario = get_object_or_404(Usuario, username=username)

    form = FormularioEquipamento()

    form_galeria = FormularioGeleriaEquipamento()

    form_tecnicas = Configuracoes.objects.last()

    form_novas_tecnicas = FormularioNovaTecnica()

    if request.method == 'POST':
        nome_do_equipamento = request.POST['nome_do_equipamento']
        apelido = request.POST['apelido']
        fabricante = request.POST['fabricante']
        url_fabricante = request.POST['url_fabricante']
        modelo = request.POST['modelo']
        descricao = request.POST['descricao']
        numero_patrimonio = request.POST['numero_patrimonio']
        tipo_de_equipamento = request.POST['tipo_de_equipamento']

        if tipo_de_equipamento != 'Preparo de Amostra':
            microscopio = True
            pre_microscopia = False
        else:
            microscopio = False
            pre_microscopia = True

        sala = request.POST['sala']

        tecnicas = {}
        for field in request.POST:
            if 'tecnica_' in field:
                for key, value in form_tecnicas.tecnicas.items():
                    if key == field:
                        tecnicas[key] = value

        equipamento = Equipamento(
            nome_do_equipamento=nome_do_equipamento,
            apelido=apelido,
            fabricante=fabricante,
            modelo=modelo,
            url_fabricante=url_fabricante,
            descricao=descricao,
            numero_patrimonio=numero_patrimonio, tipo_de_equipamento=tipo_de_equipamento,
            microscopio=microscopio,
            pre_microscopia=pre_microscopia,
            sala=sala,
            tecnicas=tecnicas
        )

        equipamento.save()

        for field in request.FILES:
            if 'profile_photo' in field:
                imagem = request.FILES['profile_photo']
                equipamento = equipamento
                descricao_da_imagem = f'Imagem de perfil do {nome_do_equipamento}'
                foto_de_perfil = True
            elif 'imagem_' in field:
                imagem = request.FILES[field]
                equipamento = equipamento
                separador = field.find("_")
                numerador = field[separador:]
                for field in request.POST:
                    if f'descricao_imagem{numerador}' in field:
                        descricao_da_imagem = request.POST[field]
                foto_de_perfil = False

            galeria = GeleriaEquipamento(
                imagem=imagem,
                equipamento=equipamento,
                descricao_da_imagem=descricao_da_imagem,
                foto_de_perfil=foto_de_perfil
            )

            galeria.save()

        for field in request.POST:
            if 'acessorio_' in field:
                if 'nome_do_acessorio_' in field:
                    nome_do_acessorio = request.POST[field]
                elif 'fabricante_do_acessorio_' in field:
                    fabricante_do_acessorio = request.POST[field]
                elif 'modelo_do_acessorio_' in field:
                    modelo_do_acessorio = request.POST[field]
                elif 'descricao_do_acessorio_' in field:
                    descricao_do_acessorio = request.POST[field]
                elif 'patrimonio_do_acessorio_' in field:
                    patrimonio_do_acessorio = request.POST[field]
                    acessorio = AcessorioEquipamento(
                        nome_do_acessorio=nome_do_acessorio,
                        fabricante=fabricante_do_acessorio,
                        modelo=modelo_do_acessorio,
                        descricao=descricao_do_acessorio,
                        numero_patrimonio=patrimonio_do_acessorio,
                        equipamento=equipamento
                    )
                    acessorio.save()

        return redirect(reverse('dashboard', args=[usuario.username]))

    dados = {
        'form': form,
        'form_galeria': form_galeria,
        'form_tecnicas': form_tecnicas,
        'form_novas_tecnicas': form_novas_tecnicas,
        'usuario': usuario,
    }

    return render(request, 'admin/dashboard/equipamentos/novo_equipamento.html', dados)


@login_required
def editar_equipamento(request, username, id_equipamento):
    usuario = get_object_or_404(Usuario, username=username)

    equipamento = get_object_or_404(Equipamento, pk=id_equipamento)

    form = FormularioEquipamento(
        data=request.POST or None, instance=equipamento)

    form_tecnicas = Configuracoes.objects.last()

    if request.method == 'POST':

        equipamento.nome_do_equipamento = redefinir_campo(
            request, 'nome_do_equipamento', equipamento.nome_do_equipamento)
        equipamento.apelido = redefinir_campo(
            request, 'apelido', equipamento.apelido)
        equipamento.fabricante = redefinir_campo(
            request, 'fabricante', equipamento.fabricante)
        equipamento.url_fabricante = redefinir_campo(
            request, 'url_fabricante', equipamento.url_fabricante)
        equipamento.modelo = redefinir_campo(
            request, 'modelo', equipamento.modelo)
        equipamento.descricao = redefinir_campo(
            request, 'descricao', equipamento.descricao)
        equipamento.numero_patrimonio = redefinir_campo(
            request, 'numero_patrimonio', equipamento.numero_patrimonio)
        equipamento.tipo_de_equipamento = redefinir_campo(
            request, 'tipo_de_equipamento', equipamento.tipo_de_equipamento)
        equipamento.sala = redefinir_campo(request, 'sala', equipamento.sala)

        if equipamento.tipo_de_equipamento != 'Preparo de Amostra':
            equipamento.microscopio = True
            equipamento.pre_microscopia = False
        else:
            equipamento.microscopio = False
            equipamento.pre_microscopia = True

        equipamento.tecnicas = {}
        for field in request.POST:
            if 'tecnica_' in field:
                for key, value in form_tecnicas.tecnicas.items():
                    if key == field:
                        equipamento.tecnicas[key] = value

        equipamento.save()

        for field in request.FILES:
            if 'profile_photo' in field:
                foto_de_perfil_do_equipamento = get_object_or_404(
                    GeleriaEquipamento, foto_de_perfil=True)
                foto_de_perfil_do_equipamento.imagem = request.FILES[field]
                foto_de_perfil_do_equipamento.save()

        for field in request.POST:
            if 'remover_imagem_' in field:
                separador = field.rfind("_")
                imagem_id = field[separador + 1:]
                imagem_para_deletar = get_object_or_404(
                    GeleriaEquipamento, pk=imagem_id)
                imagem_para_deletar.delete()

            if 'descricao_imagem_' in field:
                separador = field.rfind("_")
                imagem_id = field[separador + 1:]
                if GeleriaEquipamento.objects.filter(pk=imagem_id).exists():
                    galeria = get_object_or_404(GeleriaEquipamento, pk=imagem_id)
                    galeria.descricao_da_imagem = redefinir_campo(request, f'descricao_imagem_{imagem_id}', galeria.descricao_da_imagem)
                    
                    for file in request.FILES:
                        if f'imagem_{imagem_id}' in file:
                            galeria.imagem = request.FILES[file]
                    galeria.save()

                if not GeleriaEquipamento.objects.filter(pk=imagem_id).exists():
                    galeria = GeleriaEquipamento()
                    descricao_da_imagem = request.POST[f'descricao_imagem_{imagem_id}']
                    for file in request.FILES:
                        if f'imagem_{imagem_id}' in file:
                            imagem = request.FILES[file]
                    galeria = GeleriaEquipamento(
                        imagem=imagem,
                        equipamento=equipamento,
                        descricao_da_imagem=descricao_da_imagem,
                        foto_de_perfil=False
                    )

                    galeria.save()
        
        for field in request.POST:
            if 'remover_acessorio_' in field:
                separador = field.rfind("_")
                imagem_id = field[separador + 1:]
                imagem_para_deletar = get_object_or_404(
                    AcessorioEquipamento, pk=imagem_id)
                imagem_para_deletar.delete()

            if 'nome_do_acessorio_' in field:
                separador = field.rfind("_")
                acessorio_id = field[separador + 1:]
                if AcessorioEquipamento.objects.filter(pk=acessorio_id).exists():
                    acessorio = get_object_or_404(AcessorioEquipamento, pk=acessorio_id)
                    acessorio.nome_do_acessorio = redefinir_campo(request, f'nome_do_acessorio_{acessorio_id}', acessorio.nome_do_acessorio)
                    acessorio.fabricante = redefinir_campo(request, f'fabricante_do_acessorio_{acessorio_id}', acessorio.fabricante)
                    acessorio.modelo = redefinir_campo(request, f'modelo_do_acessorio_{acessorio_id}', acessorio.modelo)
                    acessorio.descricao = redefinir_campo(request, f'descricao_do_acessorio_{acessorio_id}', acessorio.descricao)
                    acessorio.numero_patrimonio = redefinir_campo(request, f'patrimonio_do_acessorio_{acessorio_id}', acessorio.numero_patrimonio)
                    acessorio.equipamento = equipamento
                    acessorio.save()
                    

                if not AcessorioEquipamento.objects.filter(pk=acessorio_id).exists():
                    acessorio = AcessorioEquipamento()
                    nome_do_acessorio = request.POST[f'nome_do_acessorio_{acessorio_id}']
                    fabricante = request.POST[f'fabricante_do_acessorio_{acessorio_id}']
                    modelo = request.POST[f'modelo_do_acessorio_{acessorio_id}']
                    descricao = request.POST[f'descricao_do_acessorio_{acessorio_id}']
                    numero_patrimonio = request.POST[f'patrimonio_do_acessorio_{acessorio_id}']
                    acessorio = AcessorioEquipamento(
                        nome_do_acessorio=nome_do_acessorio,
                        fabricante=fabricante,
                        modelo=modelo,
                        descricao=descricao,
                        numero_patrimonio=numero_patrimonio,
                        equipamento=equipamento                        
                    )

                    acessorio.save()
                



        return redirect(reverse('listar_equipamentos', args=[usuario.username]))

    dados = {
        'usuario': usuario,
        'form': form,
        'form_tecnicas': form_tecnicas,
        'equipamento': equipamento,
    }

    return render(request, 'admin/dashboard/equipamentos/editar_equipamento.html', dados)


@login_required
def deletar_equipamento(request, username, id_equipamento):
    usuario = get_object_or_404(Usuario, username=username)

    equipamento = get_object_or_404(Equipamento, pk=id_equipamento)

    equipamento.delete()

    return redirect(reverse('listar_equipamentos', args=[usuario.username]))


def redefinir_campo(request, campo_do_formulario, campo):
    if request.POST[campo_do_formulario] != campo:
        campo = request.POST[campo_do_formulario]
    else:
        campo = campo

    return campo
