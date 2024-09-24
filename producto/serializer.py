from rest_framework import serializers
from .models import Producto, Categoria

class CategoriaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre_categoria']  # Devuelve solo el id y nombre
        # fields = '__all__'

class ProductoSerializar(serializers.ModelSerializer):
    categoria = CategoriaSerializar(read_only=True)  # Anida el serializador de categoría

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'categoria', 'stock', 'precio_venta']  # Campos necesarios
        # fields = '__all__'
