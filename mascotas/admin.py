from django.contrib import admin
from .models import Mascota
# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'estado', 'publicado')
    list_editable = ('publicado',)
    list_filter = ('publicado', 'estado', 'tipo')


admin.site.register(Mascota)