from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.utils import simplejson

# Create your views here.
def get_horarios(request):

    idUsuario = request.session["user"]
    print idUsuario.usuIdUsuario
    t = get_template('horarios.html')

    html = t.render(Context({'usuario': idUsuario}))
    return HttpResponse(html)

def get_situacion_academica(request):

   
    t = get_template('situacionAcademica.html')
    
    html = t.render(Context({}))
    return HttpResponse(html)
