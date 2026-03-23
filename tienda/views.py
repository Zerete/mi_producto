
from .models import Producto
from .serializers import ProductoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})


class ProductoAPIView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)