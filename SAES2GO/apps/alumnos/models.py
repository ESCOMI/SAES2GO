from django.db import models

class Materia(models.Model):
    matIdMateria = models.IntegerField(primary_key=True, db_column='matIdMateria') # Field name made lowercase.
    matNombre = models.CharField(max_length=135, db_column='matNombre') # Field name made lowercase.
    matNumCreditos = models.FloatField(db_column='matNumCreditos') # Field name made lowercase.
    matArea = models.CharField(max_length=135, db_column='matArea') # Field name made lowercase.
    matNumNivel = models.IntegerField(db_column='matNumNivel') # Field name made lowercase.
    class Meta:
        db_table = u'Materias'