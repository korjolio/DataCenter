from django.contrib import admin
from.models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('publicacion', 'actualizacion')

admin.site.register(Servicio, ServicioAdmin)
