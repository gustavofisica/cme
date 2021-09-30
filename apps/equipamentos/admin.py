from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Equipamento, GeleriaEquipamento, AcessorioEquipamento

# Register your models here.
class ImagemInline(admin.TabularInline):
    model = GeleriaEquipamento

class AcessorioInline(admin.StackedInline):
    model = AcessorioEquipamento

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    inlines = [
        ImagemInline,
        AcessorioInline
    ]
