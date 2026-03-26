from django.urls import path
from .views import lista_mascota,registrar_mascota ,MascotaAPIView

urlpatterns = [
    path('', lista_mascota, name='lista_mascota'),
    path('registrar/', registrar_mascota, name='registrar_mascota'),
    path('api/mascotas/', MascotaAPIView.as_view(), name='mascota_api'),
]   