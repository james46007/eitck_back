# from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from .serializers import CajaSerializer, PedidoSerializer, PedidosSerializer, DeliverySerializer
from .models import Caja, Pedido, Imagen

from usuario.models import Usuario

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

# Create your views here.
class CajaAPI(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    @extend_schema(
        request=CajaSerializer,
        responses={201: CajaSerializer},
    )
    def post(self, request, format=None):
        """
        Crea una caja con varias images, se debe enviar un array de objetos con las imagenes
        """
        # Crear caja
        serializer = CajaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    @extend_schema(
        request=CajaSerializer,
        responses={200: CajaSerializer},
    )
    def get(self, request, format=None):
        """
        Lista las cajas
        """
        filters={"state":"1"}
        query = Caja.objects.filter(**filters).order_by('-created_at')
        serializer = CajaSerializer(query, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class PedidoAPI(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    @extend_schema(
        request=PedidoSerializer,
        responses={201: PedidoSerializer},
    )
    def post(self, request, format=None):
        """
        Crea un pedido con un array de los id de las cajas
        """
        # Actulizo datos del usuario
        usuario = Usuario.objects.get(pk=request.data['usuario'])
        usuario.nombre = request.data['nombre']
        usuario.telefono = request.data['telefono']
        if request.data['direccion'] not in usuario.direcciones:
            usuario.direcciones.append(str(request.data['direccion']))            
        usuario.save()
        # Guardar pedido
        serializer = PedidoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    @extend_schema(
        request=PedidoSerializer,
        responses={200: PedidoSerializer},
    )
    def get(self, request, format=None):
        """
        Lista los pedidos para el administrador
        """
        filters={"state":"1"}
        query = Pedido.objects.filter(**filters).order_by('-created_at')
        serializer = PedidosSerializer(query, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class DeliveryAPI(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    @extend_schema(
        request=DeliverySerializer,
        responses={200: DeliverySerializer},
    )
    def get(self, request, format=None):
        """
        Lista los pedidos para el delivery
        """
        filters={"state":"1"}
        query = Pedido.objects.filter(**filters).order_by('-created_at')
        serializer = DeliverySerializer(query, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)