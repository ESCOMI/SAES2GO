from SAES2GO.apps.seguridad.models import Usuario
from SAES2GO.apps.seguridad.models import Perfil
from django.contrib import admin


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre','apellidoPaterno','apellidoMaterno')

    def apellidoPaterno(self):
    	return self.apellidoPaterno

    def apellidoMaterno(self):
    	return self.apellidoMaterno

admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Perfil,UsuarioAdmin)
