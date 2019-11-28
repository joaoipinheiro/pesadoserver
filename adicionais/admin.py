from django.contrib import admin
from adicionais.models import Adicionais


@admin.register(Adicionais)
class AdicionaisAdmin(admin.ModelAdmin):
    model = Adicionais