from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del producto
    descripcion = models.TextField(blank=True)  # Descripción del producto (opcional)
    codigo_barras = models.CharField(max_length=50, unique=True)  # Código de barras único
    categoria = models.CharField(max_length=50)  # Categoría del producto (ej: Bebidas)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)  # Precio de venta
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)  # Precio de compra
    stock = models.IntegerField()  # Cantidad en stock
    medida = models.CharField(max_length=20)  # Unidad de medida (ej: unidades, litros)
    caducidad = models.DateField(null=True, blank=True)  # Fecha de caducidad (opcional)
    fecha_ingreso = models.DateField(auto_now_add=True)  # Fecha de ingreso al producto
    proveedor = models.CharField(max_length=100)  # Proveedor del producto
    stado = models.CharField(max_length=20, default='activo')  # Estado del producto
    image_url = models.URLField(max_length=255, blank=True)  # URL de la imagen del producto (opcional)
    impuesto = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Impuestos aplicables
    ubicacion = models.CharField(max_length=100)  # Ubicación en el almacén
    marca = models.CharField(max_length=50, blank=True)  # Marca del producto (opcional)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Descuentos aplicables

    def __str__(self):
        return self.nombre  # Esto define cómo se mostrará el objeto en el admin de Django
