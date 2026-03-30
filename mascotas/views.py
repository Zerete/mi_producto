from django.shortcuts import render , redirect
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mascota
from .serializers import MascotaSerializer


def registrar_mascota(request):
    if request.method == 'POST':
    
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        estado = request.POST.get('estado')
        raza = request.POST.get('raza')
        color = request.POST.get('color')
        ubicacion = request.POST.get('ubicacion')
        datos_contacto = request.POST.get('datos_contacto')
        foto = request.FILES.get('foto') 

        
        Mascota.objects.create(
            nombre=nombre,
            tipo=tipo,
            estado=estado,
            raza=raza,
            color=color,
            ubicacion=ubicacion,
            datos_contacto=datos_contacto,
            foto=foto, 
            vacunas = request.POST.get('vacunas') == 'on',
            tiene_chip = request.POST.get('tiene_chip') == 'on',
            latitud = request.POST.get('latitud'),
            longitud = request.POST.get('longitud'),
        )
        messages.success(request, '¡Gracias! Tu reporte ha sido recibido y será revisado por nuestro equipo antes de publicarse🐾.')
        return redirect('lista_mascota')

    return render(request, 'registrar_mascota.html')



def lista_mascota(request):
    mascotas = Mascota.objects.filter(publicado=True)
    return render(request, 'mascota.html', {'mascotas': mascotas})

class MascotaAPIView(APIView):
    def get(self, request):
        mascotas = Mascota.objects.filter(publicado=True)
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)