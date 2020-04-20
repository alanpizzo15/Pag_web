from django.db import models

# Create your models here.

class Origen(models.Model):
	pais = models.CharField(max_length=40)
	departamento = models.CharField(max_length=60)
	ciudad = models.CharField(max_length=90)

	class Meta:
		ordering = ["pais"]
		verbose_name_plural = "Origenes"

	def __str__(self):
		return self.pais


class Marca(models.Model):
	nombre = models.CharField(max_length=90)
	lugar = models.ForeignKey(Origen, on_delete=models.CASCADE)
	sitioweb = models.URLField()
	email = models.EmailField(blank=True, verbose_name='Correo Electrónico')

	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Marcas"

	def __str__(self): 
		return "%s %s" % (self.nombre, self.lugar)


class Variedad(models.Model):
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
	estilo = models.CharField(max_length=50)
	aroma = models.CharField(max_length=50)
	sabor = models.CharField(max_length=50)
	precio = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	portada = models.ImageField(upload_to='portadas')


	class Meta:
		ordering = ["estilo"]
		verbose_name_plural = "Variedades"

	def __str__(self):
		return self.estilo
