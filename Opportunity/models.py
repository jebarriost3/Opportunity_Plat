from django.db import models

# Create your models here.
# En Opportunity/models.py

from django.db import models

class Egresado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    # Agrega otros campos según tus necesidades

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
