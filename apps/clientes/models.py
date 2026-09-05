from django.db import models


class Clientes(models.Model):
	name = models.CharField(max_length=50, null=True)
	last_name = models.CharField(max_length=50, null=True)
	tipo_usuario = models.CharField(max_length=50, null=True)

	def __str__(self):
		return f'{self.name}'
