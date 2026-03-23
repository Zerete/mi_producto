from django.urls import path
from .views import lista_productos, ProductoAPIView

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('api/productos/', ProductoAPIView.as_view(), name='producto_api'),
]