from django.db import models

# Create your models here.
class Mascota(models.Model):
    ESTADO_CHOICES = [
        ('PERDIDO', 'Perdido'),
        ('ENCONTRADO', 'Encontrado'),
    ]
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    raza = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    fecha_reporte = models.DateTimeField(auto_now_add=True) 
    datos_contacto = models.TextField() 
def __str__(self):
        return f"{self.nombre if self.nombre else 'Sin nombre'} - {self.estado}"