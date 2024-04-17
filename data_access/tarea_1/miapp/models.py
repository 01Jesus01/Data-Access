from django.db import models

# Create your models here.
class WebHeros(models.Model):
    primer_name = models.CharField(max_length=15)
    primer_lastname = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    tel = models.CharField(max_length=15)

    # Representar el registro como cadena de texto
    def __str__(self):
        return self.correo