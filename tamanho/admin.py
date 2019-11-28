from django.contrib import admin
from tamanho.models import Tamanho


@admin.register(Tamanho)
class TamanhoAdmin(admin.ModelAdmin):
    model = Tamanho