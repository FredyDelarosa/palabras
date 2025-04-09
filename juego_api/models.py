from django.db import models

class Palabra(models.Model):
    NIVELES = (
        (1, 'Letras'),
        (2, 'Palabras Incompletas'),
        (3, 'Palabras Completas con Pista'),
    )

    texto = models.CharField(max_length=100)
    nivel = models.IntegerField(choices=NIVELES)
    pista = models.CharField(max_length=255, blank=True, null=True)
    imagen_url = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    anwser = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.texto
