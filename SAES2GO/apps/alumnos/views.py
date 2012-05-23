from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core import serializers
from django.utils import simplejson
from SAES2GO.apps.alumnos.models import Materia

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


def get_situacion_academica(request):
   
    t = get_template('situacionAcademica.html')
    
    html = t.render(Context({}))
    return HttpResponse(html)
