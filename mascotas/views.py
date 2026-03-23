from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mascota
from .serializers import MascotaSerializer

def lista_mascota(request):
    mascotas = Mascota.objects.all() 
    return render(request, 'mascota.html', {'mascotas': mascotas})

class MascotaAPIView(APIView):
    def get(self, request):
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)