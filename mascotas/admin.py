from django.contrib import admin
from .models import Mascota, ReporteHallazgo

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'estado', 'publicado')
    list_editable = ('publicado',)
    list_filter = ('publicado', 'estado', 'tipo')
    search_fields = ('nombre', 'raza')

class ReporteHallazgoAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'fecha_reporte', 'revisado')
    list_filter = ('revisado',)
    readonly_fields = ('mascota', 'foto_evidencia', 'comentario', 'fecha_reporte')

admin.site.register(Mascota, MascotaAdmin)
admin.site.register(ReporteHallazgo, ReporteHallazgoAdmin) 