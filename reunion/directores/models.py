from django.db import models

# Create your models here.

class Ut(models.Model):
    claveUt = models.AutoField(verbose_name = "Clave",primary_key=True) 
    nombreUt = models.CharField(max_length=300,verbose_name = "Nombre",null=False,blank=False)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "Universidad"
        verbose_name_plural = "Universidades"
        ordering = ["-claveUt"]

    def __str__(self):
        return self.nombreUt

class Director(models.Model):
    clave = models.AutoField(verbose_name = "Clave",primary_key=True) 
    nombre = models.CharField(max_length=200,verbose_name = "Nombre",null=False,blank=False)
    apPat = models.CharField(max_length=200, verbose_name = "Apellido Paterno",null=False,blank=False)
    apMat = models.CharField(max_length=200, verbose_name="Apellido Materno",null=True,blank=True)
    correo = models.CharField(max_length=200,verbose_name = "Correo",null=False,blank=False)
    telefono = models.CharField(max_length=25,verbose_name = "Teléfono",null=False,blank=False)
    grado = models.TextField(max_length=200,verbose_name = "Grado",null=False,blank=False)
    siglas = models.TextField(max_length=10,verbose_name = "Siglas de Grado",null=False,blank=False)
    claveUt = models.ForeignKey(Ut, on_delete=models.CASCADE)
    puesto = models.TextField(max_length=200,verbose_name = "Puesto",null=False,blank=False)
    status = models.BooleanField(verbose_name = "Asistencia", null=False)
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de edición")
    
    class Meta:
        verbose_name = "director"
        verbose_name_plural = "directores"
        ordering = ["-clave"]

    def __str__(self):
        return self.nombre

    



