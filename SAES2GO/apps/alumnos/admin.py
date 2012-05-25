from SAES2GO.apps.alumnos.models import Materia
from SAES2GO.apps.alumnos.models import DependenciasMateria
from SAES2GO.apps.alumnos.models import Grupo
from SAES2GO.apps.alumnos.models import Profesor
from SAES2GO.apps.alumnos.models import ProfesorMateria
from django.contrib import admin

class DependenciasMateriaAdmin(admin.ModelAdmin):
    list_display = ('materia', 'materiaRequisito','tipoDependencia')

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creditos','nivel')

admin.site.register(Materia,MateriaAdmin)
admin.site.register(DependenciasMateria,DependenciasMateriaAdmin)
admin.site.register(Grupo)
admin.site.register(Profesor)
admin.site.register(ProfesorMateria)
