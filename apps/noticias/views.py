from django.db.models import Q
from django.db.models.query_utils import Q
from django_summernote.models import Attachment
from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Noticia
from configuracoes.models import Configuracoes
from contas.models import Usuario
from noticias.forms import FormularioNoticia
from django.urls import reverse
from django.conf import settings

# Views do Site


def noticia(request, slug):
    """Renderiza uma única notícia"""
    noticia = get_object_or_404(Noticia, slug=slug)
    categorias = Noticia.ESCOLHAS_CATEGORIA
    lista_categorias = lista_de_categorias(categorias)

    dados = {
        'noticia': noticia,
        'categorias': lista_categorias,
    }

    return render(request, 'noticias/noticia.html', dados)


def lista_noticias(request, categoria):
    """Mostra uma lista de notícias classificada por categoria"""
    if categoria == 'todas':
        noticias = Noticia.objects.order_by('-edicao').all()
    else:
        noticias = Noticia.objects.order_by(
            '-edicao').filter(categoria=categoria)

    configuracoes = Configuracoes.objects.last()
    numero_de_noticias_renderizadas = configuracoes.noticias_index
    categorias = Noticia.ESCOLHAS_CATEGORIA
    lista_categorias = lista_de_categorias(categorias)

    paginator = Paginator(noticias, numero_de_noticias_renderizadas)
    page = request.GET.get('page')
    noticias_por_pagina = paginator.get_page(page)

    dados = {
        'noticias': noticias_por_pagina,
        'categorias': lista_categorias,
    }

    return render(request, 'noticias/lista_noticias.html', dados)


# Views do Dashboard

@login_required
def nova_noticia(request, username):
    """Criar uma nova notícia"""

    usuario = get_object_or_404(Usuario, username=username)

    form = FormularioNoticia(request.POST)

    if request.method == 'POST':

        if form.is_valid():

            form = form.save(commit=False)

            form.autor = usuario

            form.save()

            return redirect(reverse('noticias', args=[usuario.username]))

    else:

        dados = {
            'usuario': usuario,
            'form': form
        }

        return render(request, 'admin/dashboard/noticias/nova_noticia.html', dados)


@ login_required
def noticias(request, username):

    usuario = get_object_or_404(Usuario, username=username)

    noticias = Noticia.objects.order_by('-edicao').all()

    if request.method == 'POST':

        noticias = Noticia.objects.filter(
            Q(titulo__icontains=request.POST['table_search']) |
            Q(texto__icontains=request.POST['table_search']) |
            Q(categoria__icontains=request.POST['table_search'])
        )

    configuracoes = Configuracoes.objects.last()

    numero_de_noticias_renderizadas = configuracoes.noticias_index

    paginator = Paginator(noticias, numero_de_noticias_renderizadas)

    page = request.GET.get('page')

    noticias_por_pagina = paginator.get_page(page)

    dados = {
        'usuario': usuario,
        'noticias': noticias_por_pagina,
    }

    return render(request, 'admin/dashboard/noticias/lista_noticias.html', dados)


@login_required
def editar_noticia(request, username, slug):

    usuario = get_object_or_404(Usuario, username=username)

    noticia = get_object_or_404(Noticia, slug=slug)

    form = FormularioNoticia(data=request.POST or None, instance=noticia)

    if request.method == 'POST':

        if form.is_valid():

            form.save()

            return redirect(reverse('noticias', args=[usuario.username]))

    dados = {
        'usuario': usuario,
        'form': form,
        'noticia': noticia,
    }

    return render(request, 'admin/dashboard/noticias/editar_noticia.html', dados)


@login_required
def deletar_noticia(request, username, slug):

    usuario = get_object_or_404(Usuario, username=username)

    noticia = get_object_or_404(Noticia, slug=slug)

    deletar_arquivos_da_noticia(noticia)

    noticia.delete()

    return redirect(reverse('noticias', args=[usuario.username]))

# Funções auxiliares


def lista_de_categorias(categorias):
    """Retorna uma lista de categorias de notícias"""
    lista_categorias = []

    for categoria in categorias:
        lista_categorias.append(categoria[0])

    return lista_categorias


def deletar_arquivos_da_noticia(noticia):
    texto = BeautifulSoup(noticia.texto, 'lxml')

    imagens = texto.find_all('img')

    if imagens:

        for imagem in imagens:

            src = str(imagem['src'])

            file = src.removeprefix('/media/')

            if Attachment.objects.filter(file=file).exists():

                arquivo = get_object_or_404(Attachment, file=file)

                print(arquivo)

                arquivo.file.delete()

                arquivo.delete()
