from django.db import models

class Perfil(models.Model):
    perIdPerfil = models.IntegerField(primary_key=True, db_column='perIdPerfil')
    perNombre = models.CharField(max_length=135, db_column='perNombre')
    class Meta:
        db_table = u'Perfiles'

class Usuario(models.Model):
    usuIdUsuario = models.CharField(max_length=135, primary_key=True, db_column='usuIdUsuario')
    perIdPerfil = models.ForeignKey(Perfil, db_column='perIdPerfil')
    usuNombre = models.CharField(max_length=135, db_column='usuNombre', blank=True)
    usuAPaterno = models.CharField(max_length=135, db_column='usuAPaterno', blank=True)
    usuaAMaterno = models.CharField(max_length=135, db_column='usuAMaterno', blank=True)
    usuPassword = models.CharField(max_length=135, db_column='usuPassword')
    class Meta:
        db_table = u'Usuarios'

