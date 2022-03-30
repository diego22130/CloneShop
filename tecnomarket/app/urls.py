from unicodedata import name
from django.urls import path, include
from .views import MarcaViewset, home, contacto, galeria, agregar_producto, listar_producto, \
    modificar_producto, eliminar_producto, registro, ProductoViewset, MarcaSerializer

from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('marca', MarcaViewset)

urlpatterns = [
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
    path('producto/agregar/', agregar_producto, name='agregarProducto'),
    path('producto/listar/', listar_producto, name='listarProducto'),
    path('producto/modificar/<id>/', modificar_producto, name='modificarProducto'),
    path('producto/eliminar/<id>/', eliminar_producto, name='eliminarProducto'),
    path('registro/', registro, name='registro'),
    path('api/', include(router.urls)),
]