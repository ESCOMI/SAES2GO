from django.db import models
from SAES2GO.apps.seguridad.models import Usuario



class Materia(models.Model):
    id = models.AutoField(primary_key=True, db_column='matIdMateria')
    nombre = models.CharField(max_length=135, db_column='matNombre')
    creditos = models.FloatField(db_column='matNumCreditos')
    area = models.CharField(max_length=135, db_column='matArea')
    nivel = models.IntegerField(db_column='matNumNivel')
    semestre = models.CharField(max_length=1, db_column='matTipoSemestre')
    class Meta:
        db_table = u'Materias'
        ordering = ('nombre',)        

    def get_dependencias(self):        
        
        dependencias = DependenciasMateria.objects.filter(materia = self.id)       
        
        listdependencias = []
        for dependencia in dependencias:
            listdependencias.append({'materiaRequisito':int(dependencia.materiaRequisito.id),'tipoDependencia':dependencia.tipoDependencia.encode('utf-8')})

        return listdependencias

    def __unicode__(self):
        return self.nombre


class DependenciasMateria(models.Model):
    id = models.AutoField(primary_key=True, db_column='depmIdDependencia')
    materia = models.ForeignKey(Materia, db_column='matIdMateria',related_name="materiaOriginal")
    materiaRequisito = models.ForeignKey(Materia, db_column='matIdMateriaRequisito',related_name="materiaDependiente")
    tipoDependencia = models.CharField(max_length=135, db_column='matTipoDependencia')
    class Meta:
        db_table = u'DependenciasMateria'
        verbose_name_plural = 'Dependencias de Materia'
        ordering = ('materia','tipoDependencia',)  


    def toJSON(self):
        return '{"requisito":'+str(self.materiaRequisito.id)+',"tipo","'+str(self.tipoDependencia)+'"}'

    def __unicode__(self):
        return self.materia.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=18, primary_key=True, db_column='gruIdGrupo')
    numero = models.IntegerField(db_column='gruNumGrupo')
    turno = models.CharField(max_length=3, db_column='gruTurno')
    class Meta:
        db_table = u'Grupos'
        ordering = ('numero','turno',)

    def __unicode__(self):
        return self.nombre

class Profesor(models.Model):
    cedula = models.IntegerField(primary_key=True, db_column='profCedulaProfesor')
    usuario = models.ForeignKey(Usuario, db_column='usuIdUsuario')
    class Meta:
        db_table = u'Profesores'
        verbose_name_plural = "Profesores"


    def __unicode__(self):
        return self.nombre

class ProfesorMateria(models.Model):
    id = models.AutoField(primary_key=True, db_column='profmIdProfesorMateria')
    profesor = models.ForeignKey(Profesor, db_column='profCedulaProfesor')
    materia = models.ForeignKey(Materia, db_column='Materias_matIdMateria')
    class Meta:
        db_table = u'ProfesoresMateria'
        verbose_name_plural = 'Materias de Profesor'
        ordering = ('profesor__nombre','materia__nombre',)

    def __unicode__(self):
        return self.profesor.nombre+' - '+self.materia.nombre

class TipoHorario(models.Model):
    tihidtipohorario = models.AutoField(primary_key=True, db_column='tihIdTipoHorario') # Field name made lowercase.
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


class MateriaGrupo(models.Model):
    id = models.AutoField(primary_key=True, db_column='matgIdMateriaGrupo')
    materia = models.ForeignKey(Materia, db_column='matIdMateria')
    grupo = models.ForeignKey(Grupo, db_column='gruIdGrupo')
    profesor = models.ForeignKey(Profesor, db_column='profCedulaProfesor')
    anio = models.IntegerField(db_column='matgAnio')
    semestre = models.CharField(max_length=3, db_column='matgTipoSemestre')
    lugaresDisponibles = models.IntegerField(db_column='magtLugaresDisp')
    salon = models.IntegerField(db_column='matgSalon')
    tipoHorario = models.ForeignKey(TipoHorario, db_column='tihIdTipoHorario')
    class Meta:
        db_table = u'MateriasGrupo'

    
        