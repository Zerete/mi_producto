from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mascota, ReporteHallazgo
from .serializers import MascotaSerializer

def registrar_mascota(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        estado = request.POST.get('estado')
        raza = request.POST.get('raza')
        ubicacion = request.POST.get('ubicacion')
        datos_contacto = request.POST.get('datos_contacto')
        foto = request.FILES.get('foto') 

        Mascota.objects.create(
            nombre=nombre,
            tipo=tipo,
            estado=estado,
            raza=raza,
            ubicacion=ubicacion,
            datos_contacto=datos_contacto,
            foto=foto,
            vacunas=request.POST.get('vacunas') == 'on',
            tiene_chip=request.POST.get('tiene_chip') == 'on',
            color="No especificado", 
            publicado=False 
        )
        messages.success(request, '¡Gracias! Tu reporte ha sido recibido🐾.')
        return redirect('lista_mascota')

    return render(request, 'registrar_mascota.html')

def marcar_encontrado(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    
    if request.method == 'POST':
        ReporteHallazgo.objects.create(
            mascota=mascota,
            foto_evidencia=request.FILES.get('foto_prueba'),
            comentario=request.POST.get('detalle_hallazgo')
        )
        messages.success(request, f'¡Pruebas enviadas! Revisaremos el hallazgo de {mascota.nombre} pronto. 🎉')
    
    return redirect('lista_mascota')

def lista_mascota(request):
    mascotas = Mascota.objects.filter(publicado=True)
    return render(request, 'mascota.html', {'mascotas': mascotas})

class MascotaAPIView(APIView):
    def get(self, request):
        mascotas = Mascota.objects.filter(publicado=True)
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)