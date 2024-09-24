from rest_framework import viewsets
from .serializer import ProductoSerializar
from .models import Producto

class ProductoView(viewsets.ModelViewSet):

    serializer_class = ProductoSerializar

    queryset = Producto.objects.all()