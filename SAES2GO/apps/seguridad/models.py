from django.db import models

class Perfil(models.Model):
    id = models.AutoField(primary_key=True, db_column='perIdPerfil')
    nombre = models.CharField(max_length=135, db_column='perNombre')
    class Meta:
        db_table = u'Perfiles'
        verbose_name_plural = "Perfiles"

    def __unicode__(self):
        return str(self.id)+'-'+self.nombre
    

class Usuario(models.Model):
    id = models.CharField(max_length=135, primary_key=True, db_column='usuIdUsuario')
    perfil = models.ForeignKey(Perfil, db_column='perIdPerfil')
    nombre = models.CharField(max_length=135, db_column='usuNombre', blank=True)
    apellidoPaterno = models.CharField(max_length=135, db_column='usuAPaterno', blank=True)
    apellidoMaterno = models.CharField(max_length=135, db_column='usuAMaterno', blank=True)
    password = models.CharField(max_length=135, db_column='usuPassword')
    class Meta:
        db_table = u'Usuarios'

    def __unicode__(self):
        return str(self.id)

