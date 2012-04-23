from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core import serializers
from SAES2GO.apps.alumnos.models import Materia

# Create your views here.
def get_horarios(request):

    idUsuario = request.session["user"]
    print idUsuario.usuIdUsuario
    t = get_template('horarios.html')

    html = t.render(Context({'usuario': idUsuario}))
    return HttpResponse(html)


def get_materias(request):

    materias = serializers.serialize('json', Materia.objects.all(), fields=('matNombre','matNumNivel'))
    return HttpResponse(materias, mimetype="application/x-javascript")


def get_situacion_academica(request):

   
    t = get_template('situacionAcademica.html')
    
    html = t.render(Context({}))
    return HttpResponse(html)
