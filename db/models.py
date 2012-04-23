# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Actividades(models.Model):
    actidactividad = models.IntegerField(primary_key=True, db_column='actIdActividad') # Field name made lowercase.
    matgidmateriagrupo = models.ForeignKey(Materiasgrupo, db_column='matgIdMateriaGrupo') # Field name made lowercase.
    actnombre = models.CharField(max_length=135, db_column='actNombre') # Field name made lowercase.
    actnummiembros = models.IntegerField(db_column='actNumMiembros') # Field name made lowercase.
    actfchainicio = models.DateField(db_column='actFchaInicio') # Field name made lowercase.
    actfechalimite = models.DateField(null=True, db_column='actFechaLimite', blank=True) # Field name made lowercase.
    actespecificaciones = models.CharField(max_length=765, db_column='actEspecificaciones') # Field name made lowercase.
    class Meta:
        db_table = u'Actividades'

class Actividadesalumno(models.Model):
    aluboletaalumno = models.ForeignKey(Alumnos, db_column='aluBoletaAlumno') # Field name made lowercase.
    actidactividad = models.ForeignKey(Actividades, db_column='actIdActividad') # Field name made lowercase.
    matgidmateriagrupo = models.ForeignKey(Actividades, db_column='matgIdMateriaGrupo') # Field name made lowercase.
    acalnumequipo = models.IntegerField(null=True, db_column='acalNumEquipo', blank=True) # Field name made lowercase.
    acalcalificacion = models.FloatField(null=True, db_column='acalCalificacion', blank=True) # Field name made lowercase.
    acalfechaentrega = models.DateField(null=True, db_column='acalFechaEntrega', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ActividadesAlumno'

class Alumnos(models.Model):
    aluboletaalumno = models.IntegerField(primary_key=True, db_column='aluBoletaAlumno') # Field name made lowercase.
    usuidusuario = models.ForeignKey(Usuarios, db_column='usuIdUsuario') # Field name made lowercase.
    alumateriasreprobadas = models.IntegerField(db_column='aluMateriasReprobadas') # Field name made lowercase.
    alumateriasdesfasadas = models.IntegerField(db_column='aluMateriasDesfasadas') # Field name made lowercase.
    alucreditosadquiridos = models.FloatField(db_column='aluCreditosAdquiridos') # Field name made lowercase.
    class Meta:
        db_table = u'Alumnos'

class Elementosmultimedia(models.Model):
    mulidelemento = models.IntegerField(primary_key=True, db_column='mulIdElemento') # Field name made lowercase.
    matgidmateriagrupo = models.ForeignKey(Materiasgrupo, db_column='matgIdMateriaGrupo') # Field name made lowercase.
    mulfechaclase = models.DateField(db_column='mulFechaClase') # Field name made lowercase.
    multipomultimedia = models.CharField(max_length=135, db_column='mulTipoMultimedia') # Field name made lowercase.
    class Meta:
        db_table = u'ElementosMultimedia'

class Gestores(models.Model):
    gesclavegestor = models.CharField(max_length=135, primary_key=True, db_column='gesClaveGestor') # Field name made lowercase.
    usuidusuario = models.ForeignKey(Usuarios, db_column='usuIdUsuario') # Field name made lowercase.
    class Meta:
        db_table = u'Gestores'

class Grupos(models.Model):
    gruidgrupo = models.CharField(max_length=18, primary_key=True, db_column='gruIdGrupo') # Field name made lowercase.
    grunumgrupo = models.IntegerField(db_column='gruNumGrupo') # Field name made lowercase.
    gruturno = models.CharField(max_length=3, db_column='gruTurno') # Field name made lowercase.
    class Meta:
        db_table = u'Grupos'

class Horariosalumno(models.Model):
    halidhorarioalumno = models.IntegerField(primary_key=True, db_column='halIdHorarioAlumno') # Field name made lowercase.
    aluboletaalumno = models.ForeignKey(Alumnos, db_column='aluBoletaAlumno') # Field name made lowercase.
    matgidmateriagrupo = models.ForeignKey(Materiasgrupo, db_column='matgIdMateriaGrupo') # Field name made lowercase.
    haldificultad = models.IntegerField(null=True, db_column='halDificultad', blank=True) # Field name made lowercase.
    halcalificacion = models.FloatField(null=True, db_column='halCalificacion', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'HorariosAlumno'

class Materias(models.Model):
    matidmateria = models.IntegerField(primary_key=True, db_column='matIdMateria') # Field name made lowercase.
    matnombre = models.CharField(max_length=135, db_column='matNombre') # Field name made lowercase.
    matnumcreditos = models.FloatField(db_column='matNumCreditos') # Field name made lowercase.
    matarea = models.CharField(max_length=135, db_column='matArea') # Field name made lowercase.
    matnumnivel = models.IntegerField(db_column='matNumNivel') # Field name made lowercase.
    class Meta:
        db_table = u'Materias'

class Materiasgrupo(models.Model):
    matgidmateriagrupo = models.IntegerField(primary_key=True, db_column='matgIdMateriaGrupo') # Field name made lowercase.
    matidmateria = models.ForeignKey(Materias, db_column='matIdMateria') # Field name made lowercase.
    gruidgrupo = models.ForeignKey(Grupos, db_column='gruIdGrupo') # Field name made lowercase.
    profcedulaprofesor = models.ForeignKey(Profesores, null=True, db_column='profCedulaProfesor', blank=True) # Field name made lowercase.
    matganio = models.IntegerField(null=True, db_column='matgAnio', blank=True) # Field name made lowercase.
    matgtiposemestre = models.CharField(max_length=3, db_column='matgTipoSemestre', blank=True) # Field name made lowercase.
    matglugaresdisp = models.IntegerField(db_column='matgLugaresDisp') # Field name made lowercase.
    matgsalon = models.IntegerField(null=True, db_column='matgSalon', blank=True) # Field name made lowercase.
    tihidtipohorario = models.ForeignKey(Tiposhorario, db_column='tihIdTipoHorario') # Field name made lowercase.
    class Meta:
        db_table = u'MateriasGrupo'

class Mensajes(models.Model):
    menidmensaje = models.IntegerField(primary_key=True, db_column='menIdMensaje') # Field name made lowercase.
    mentexto = models.CharField(max_length=765, db_column='menTexto') # Field name made lowercase.
    usuidusuarioorigen = models.ForeignKey(Usuarios, db_column='usuIdUsuarioOrigen') # Field name made lowercase.
    usuidusuariodestino = models.ForeignKey(Usuarios, db_column='usuIdUsuarioDestino') # Field name made lowercase.
    class Meta:
        db_table = u'Mensajes'

class Perfiles(models.Model):
    peridperfil = models.IntegerField(primary_key=True, db_column='perIdPerfil') # Field name made lowercase.
    pernombre = models.CharField(max_length=135, unique=True, db_column='perNombre') # Field name made lowercase.
    class Meta:
        db_table = u'Perfiles'

class Profesores(models.Model):
    profcedulaprofesor = models.IntegerField(primary_key=True, db_column='profCedulaProfesor') # Field name made lowercase.
    usuidusuario = models.ForeignKey(Usuarios, db_column='usuIdUsuario') # Field name made lowercase.
    class Meta:
        db_table = u'Profesores'

class Temarios(models.Model):
    temidtema = models.CharField(max_length=15, primary_key=True, db_column='temIdTema') # Field name made lowercase.
    matidmateria = models.ForeignKey(Materias, db_column='matIdMateria') # Field name made lowercase.
    temidtemapadre = models.ForeignKey('self', db_column='temIdTemaPadre') # Field name made lowercase.
    temnombre = models.CharField(max_length=135, db_column='temNombre') # Field name made lowercase.
    class Meta:
        db_table = u'Temarios'

class Tiposhorario(models.Model):
    tihidtipohorario = models.IntegerField(primary_key=True, db_column='tihIdTipoHorario') # Field name made lowercase.
    tihhorainilunes = models.CharField(max_length=135, db_column='tihHoraIniLunes', blank=True) # Field name made lowercase.
    tihduracionlunes = models.IntegerField(null=True, db_column='tihDuracionLunes', blank=True) # Field name made lowercase.
    tihhorainimartes = models.CharField(max_length=135, db_column='tihHoraIniMartes', blank=True) # Field name made lowercase.
    tihduracionmartes = models.IntegerField(null=True, db_column='tihDuracionMartes', blank=True) # Field name made lowercase.
    tihhorainimiercoles = models.CharField(max_length=135, db_column='tihHoraIniMiercoles', blank=True) # Field name made lowercase.
    tihduracionmiercoles = models.IntegerField(null=True, db_column='tihDuracionMiercoles', blank=True) # Field name made lowercase.
    tihhorainijueves = models.CharField(max_length=135, db_column='tihHoraIniJueves', blank=True) # Field name made lowercase.
    tihduracionjueves = models.IntegerField(null=True, db_column='tihDuracionJueves', blank=True) # Field name made lowercase.
    tihhorainiviernes = models.CharField(max_length=135, db_column='tihHoraIniViernes', blank=True) # Field name made lowercase.
    tihduracionviernes = models.IntegerField(null=True, db_column='tihDuracionViernes', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'TiposHorario'

class Usuarios(models.Model):
    usuidusuario = models.CharField(max_length=135, primary_key=True, db_column='usuIdUsuario') # Field name made lowercase.
    peridperfil = models.ForeignKey(Perfiles, db_column='perIdPerfil') # Field name made lowercase.
    usunombre = models.CharField(max_length=135, db_column='usuNombre', blank=True) # Field name made lowercase.
    usuapaterno = models.CharField(max_length=135, db_column='usuAPaterno', blank=True) # Field name made lowercase.
    usuamaterno = models.CharField(max_length=135, db_column='usuAMaterno', blank=True) # Field name made lowercase.
    usupassword = models.CharField(max_length=135, db_column='usuPassword', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Usuarios'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=240, unique=True)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=90, unique=True)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    class Meta:
        db_table = u'auth_user_user_permissions'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=600)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    app_label = models.CharField(max_length=300, unique=True)
    model = models.CharField(max_length=300, unique=True)
    class Meta:
        db_table = u'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=120, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'django_site'

class Temp(models.Model):
    grupo = models.CharField(max_length=135)
    materia = models.CharField(max_length=135)
    profesor = models.CharField(max_length=135)
    lunes = models.CharField(max_length=135)
    martes = models.CharField(max_length=135)
    miercoles = models.CharField(max_length=135)
    jueves = models.CharField(max_length=135)
    viernes = models.CharField(max_length=135)
    class Meta:
        db_table = u'temp'

