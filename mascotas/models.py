from django.db import models

# Create your models here.
class Mascota(models.Model):

    TIPO_CHOICES = [
        ('PERRO', 'Perro'),
        ('GATO', 'Gato'),
        ('OTRO', 'Otro'),
    ]
    tipo = models.CharField(
        max_length=20, 
        choices=TIPO_CHOICES, 
        default='PERRO',
        verbose_name="Tipo de Animal"
    )


    ESTADO_CHOICES = [
        ('PERDIDO', 'Perdido'),
        ('ENCONTRADO', 'Encontrado'),
    ]
    foto = models.ImageField(upload_to='mascotas/', null=True, blank=True, verbose_name="Fotografía")
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)
    raza = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    fecha_reporte = models.DateTimeField(auto_now_add=True) 
    datos_contacto = models.TextField() 
    publicado = models.BooleanField(default=False, verbose_name="¿Aprobado para publicar?")

    vacunas = models.BooleanField(default=False, verbose_name="¿Vacunado?")
    tiene_chip = models.BooleanField(default=False, verbose_name="¿Tiene Chip?")

    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre if self.nombre else 'Sin nombre'} - {self.estado}"