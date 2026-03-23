from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mascota
from .serializers import MascotaSerializer

def lista_productos(request):
    productos = Mascota.objects.all()
    return render(request, 'productos.html', {'productos': productos})

class MascotaAPIView(APIView):
    def get(self, request):
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)