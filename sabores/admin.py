from django.contrib import admin
from sabores.models import Sabores


@admin.register(Sabores)
class SaboresAdmin(admin.ModelAdmin):
    model = Sabores