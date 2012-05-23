from django.db import models


"""
class Materiasgrupo(models.Model):
    id = models.AutoField(primary_key=True, db_column='matgIdMateriaGrupo')
    materia = models.ForeignKey(Materia, db_column='matIdMateria')
    grupo = models.ForeignKey(Grupo, db_column='gruIdGrupo')
    profesor = models.ForeignKey(Profesor, db_column='profCedulaProfesor')
    anio = models.IntegerField(db_column='matgAnio')
    semestre = models.CharField(max_length=3, db_column='matgTipoSemestre')
    lugaresDisponibles = models.IntegerField(db_column='magtLugaresDisp')
    salon = models.IntegerField(db_column='matgSalon')
    tipoHorario = models.ForeignKey(TiposHorario, db_column='tihIdTipoHorario')
    class Meta:
        db_table = u'MateriasGrupo'
"""

class Materia(models.Model):
    id = models.AutoField(primary_key=True, db_column='matIdMateria')
    nombre = models.CharField(max_length=135, db_column='matNombre')
    creditos = models.FloatField(db_column='matNumCreditos')
    area = models.CharField(max_length=135, db_column='matArea')
    nivel = models.IntegerField(db_column='matNumNivel')
    semestre = models.CharField(max_length=1, db_column='matTipoSemestre')
    class Meta:
        db_table = u'Materias'        

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


    def toJSON(self):
        return '{"requisito":'+str(self.materiaRequisito.id)+',"tipo","'+str(self.tipoDependencia)+'"}'

    def __unicode__(self):
        return self.materia.nombre+' <- '+self.materiaRequisito.nombre
    
        