from django.db import models

# Create your models here.
class Aprendiz(models.Model):
    ID_aprendiz = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    Programa_formacion = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = 'aprendiz'
    
class Instructor(models.Model):
    ID_instructor=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50,null=True)
    apellido=models.CharField(max_length=50,null=True)
    especialidad=models.CharField(max_length=50,null=True)

    class Meta:
        db_table= 'instructor'


class Horario(models.Model):
    ID_horario=models.IntegerField(primary_key=True)
    dia=models.CharField(max_length=50,null=True)
    hora_inicio=models.TimeField()
    hora_fin=models.TimeField()
    
    class Meta:
        db_table='horario'

class Jornada(models.Model):
    ID_jornada=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50,null=True)
    hora_inicio=models.TimeField()
    hora_fin=models.TimeField()
    class Meta:
        db_table='jornada'
# class Cronograma(models.Model):
#     ID_cronograma=models.IntegerField(primary_key=True)
#     semana=models.IntegerField()
#     descripcion=models.CharField(max_length=90,null=True)
#     class Meta:
#         db_table='jornada'
# class Materia(models.Model):
#     ID_materia=models.IntegerField(primary_key=True)
#     nombre=models.CharField(max_length=40,null=True)
#     descripcion=models.CharField(max_length=100,null=True)
#     class Meta:
#         db_table='materia'
# class Asignado(models.Model):
#     ID_instructor=models.ForeignKey(Instructor, on_delete=models.CASCADE)
#     ID_horario=models.ForeignKey(Horario, on_delete=models.CASCADE)