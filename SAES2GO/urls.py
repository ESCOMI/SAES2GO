from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',	
    (r'^$', direct_to_template, {'template': 'base.html'}),
    (r'^validateLogin/$', 'SAES2GO.apps.seguridad.views.validate_login'),
    (r'^emailConfirmation/(.*)/(.*)/$', 'SAES2GO.apps.seguridad.views.email_confirmation'),
    (r'^alumnos/horarios/$', 'SAES2GO.apps.alumnos.views.get_horarios'),
    (r'^alumnos/situacionAcademica/progresoGeneral/$', 'SAES2GO.apps.alumnos.views.get_progresoGeneral'),
    (r'^alumnos/situacionAcademica/$', 'SAES2GO.apps.alumnos.views.get_situacion_academica'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^materias/$', 'SAES2GO.apps.alumnos.views.get_materias'),
    (r'^grupos/$', 'SAES2GO.apps.alumnos.views.get_grupos'),
    (r'^grupos/guardar/$', 'SAES2GO.apps.alumnos.views.guarda_grupo'),
    (r'^tiposHorario/$', 'SAES2GO.apps.alumnos.views.get_tipos_horario'),
    # Examples:
    # url(r'^$', 'SAES2GO.views.home', name='home'),
    # url(r'^SAES2GO/', include('SAES2GO.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
