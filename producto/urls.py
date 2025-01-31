from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from producto import views

router = routers.DefaultRouter()

router.register(r'producto', views.ProductoView, 'producto')
router.register(r'categoria', views.CategoriaView, 'categoria')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Producto API'))
]

