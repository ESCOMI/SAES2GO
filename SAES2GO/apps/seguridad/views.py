from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils import simplejson
from SAES2GO.apps.seguridad.models import Usuario
from django.core.mail import EmailMessage
import random
import string

# Create your views here.
def validate_login(request):

    idUsuario = request.GET['logUser']

    try:
        usuario = Usuario.objects.get(id__exact = idUsuario, password__exact = request.GET['logPass'])
        request.session["user"] = usuario

        t = get_template('alumnos_base.html')

        html = t.render(Context({'usuario': idUsuario}))
        return HttpResponse(html)

    except Usuario.DoesNotExist:
        usuario = None    

    return HttpResponseRedirect("http://localhost:8000")


def register_user(request):
    datos = simplejson.loads(request.GET['datos'])
    mail = datos['regMail']
    perfil = datos['regPerfil']

    confirmation_code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33))

    usuario = Usuario.objects.create(id = mail, password = confirmation_code, perfil = perfil)
    usuario.save()

    email = EmailMessage('Asunto', 'Favor de ingresar a la siguiente url para completar su registro: http://localhost:8000/emailConfirmation/'+mail+'/'+confirmation_code, to=[mail])
    email.send()

    respuesta = {'resultado': 'ok','mensaje':'Se ha enviado un mensaje de confirmacion a su correo'}
    json = simplejson.dumps(respuesta)
    return HttpResponse(json, mimetype="application/x-javascript")


def email_confirmation(request, username , confirmation_code):
    try:
        user = Usuario.objects.get(id__exact = username, password = confirmation_code)
        
    except Usuario.DoesNotExist:
        user = None

    print user.usuIdUsuario
    return render_to_response('emailConfirmation.html')