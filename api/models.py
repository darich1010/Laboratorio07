from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField("Nombre de la categoría", max_length=100)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField("Nombre del producto", max_length=100)    
    descripcion = models.TextField("Descripción", blank=True)
    precio = models.DecimalField("Precio (S/.)", max_digits=10, decimal_places=2, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
    
class Publicacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField("Descripción", blank=True)
    precio = models.DecimalField("Precio (S/.)", max_digits=10, decimal_places=2)
    fecha_publicacion = models.DateTimeField("Fecha de publicación", auto_now_add=True)

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return f"{self.producto.nombre} - S/ {self.precio}"
