from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson
from SAES2GO.apps.alumnos.models import Materia
from SAES2GO.apps.alumnos.models import Grupo
from SAES2GO.apps.alumnos.models import TipoHorario
from SAES2GO.apps.alumnos.models import MateriaGrupo
from datetime import date



# Create your views here.
def get_horarios(request):

    idUsuario = request.session["user"]
    
    t = get_template('horarios.html')

    html = t.render(Context({'usuario': idUsuario}))
    return HttpResponse(html)


def get_progresoGeneral(request):

    listmaterias = Materia.objects.order_by('-nivel','-semestre')

    materias = []

    for materia in listmaterias:
        dependencias = materia.get_dependencias() 
            
        materias.append({'id':materia.id,'nombre':materia.nombre,'nivel':materia.nivel,'semestre':materia.semestre,'dependencias':dependencias})

    materias = simplejson.dumps(materias)

    return HttpResponse(materias, mimetype="application/x-javascript")

def get_materias(request):
    
    nivel = request.GET.get('nivel', '')

    listmaterias = Materia.objects.filter(nivel = nivel).order_by('nombre')

    materias = []

    for materia in listmaterias:

        materias.append({'id':materia.id,'nombre':materia.nombre,'horas':materia.horasSemanales})

    materias = simplejson.dumps(materias)

    return HttpResponse(materias, mimetype = "application/x-javascript")

def get_grupos(request):
    
    turno = request.GET.get('turno', '')

    listgrupos = Grupo.objects.filter(turno = turno)

    grupos = []

    for grupo in listgrupos:
            
        grupos.append({'nombre':grupo.nombre})

    grupos = simplejson.dumps(grupos)

    return HttpResponse(grupos, mimetype="application/x-javascript")

def get_tipos_horario(request):

    tiposHorario = serializers.serialize('json', TipoHorario.objects.all(), fields=('id','horaLunes','duracionLunes','horaMartes','duracionMartes','horaMiercoles','duracionMiercoles','horaJueves','duracionJueves','horaViernes','duracionViernes'))

    return HttpResponse(tiposHorario, mimetype="application/x-javascript")

def get_situacion_academica(request):
   
    t = get_template('situacionAcademica.html')
    
    html = t.render(Context({}))
    return HttpResponse(html)

def guarda_grupo(request):
    grupo = request.GET.get('grupo', '')
    salon = request.GET.get('salon', '')

    fechaActual=date.today()

    materias = simplejson.loads(request.GET['materias'])

    for materia in materias:

        materiagrupo = MateriaGrupo()
        
        materiagrupo.materia = Materia.objects.get(id = int(materia.replace("mat","")))
        materiagrupo.grupo = Grupo.objects.get(nombre = grupo)
        materiagrupo.lugaresDisponibles = 30
        materiagrupo.salon = salon
        materiagrupo.anio = fechaActual.year
        materiagrupo.semestre = 'A'
        materiagrupo.tipoHorario = TipoHorario(id= int(materias[materia][0]))

        materiagrupo.save()

    resultado = simplejson.dumps({'mensaje':'Grupo registrado!'})

    return HttpResponse(resultado, mimetype="application/x-javascript")

