
from django.db import models
# Create your models here.

class Clientes(models.Model):
    name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    tipo_usuario = models.CharField(null=True, max_length=50)

    def __str__(self):
        return f'{self.name}'






