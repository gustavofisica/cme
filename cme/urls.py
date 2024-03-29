"""cme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # URLs do sitio www.cme.ufpr.br
    path('', include('sitio.urls')),
    path('equipamentos/', include('equipamentos.urls')),
    path('noticias/', include('noticias.urls')),
    path('configuracoes/', include('configuracoes.urls')),
    # URLs do Sistema de Gerenciamento
    path('sistema_de_gerenciamento/', include('contas.urls')),
    path('sistema_de_gerenciamento/', include('noticias.urls_dashboard')),
    path('sistema_de_gerenciamento/', include('equipamentos.urls_dashboard')),
    # URLs de Terceiros
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
