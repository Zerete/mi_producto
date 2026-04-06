from django.urls import path
from .views import lista_mascota, registrar_mascota, marcar_encontrado, MascotaAPIView

urlpatterns = [
    path('', lista_mascota, name='lista_mascota'),
    path('registrar/', registrar_mascota, name='registrar_mascota'),
    path('api/mascotas/', MascotaAPIView.as_view(), name='mascota_api'),
    
    path('marcar-encontrado/<int:mascota_id>/', marcar_encontrado, name='marcar_encontrado'),
]