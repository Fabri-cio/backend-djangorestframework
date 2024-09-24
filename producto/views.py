from rest_framework import viewsets
from .serializer import ProductoSerializar, CategoriaSerializar
from .models import Producto, Categoria

class CategoriaView(viewsets.ModelViewSet):
    serializer_class=CategoriaSerializar
    queryset = Categoria.objects.all()

class ProductoView(viewsets.ModelViewSet):

    serializer_class = ProductoSerializar

    queryset = Producto.objects.all()
