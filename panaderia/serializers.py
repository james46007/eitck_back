from rest_framework import serializers

from .models import Caja, Pedido, Imagen

# User Serializer

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ['imagen']

class CajaSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(many=True,allow_empty=True)
    class Meta:
        model = Caja
        fields = '__all__'

    def create(self, validated_data):
        cajas_data = validated_data.pop('imagenes')
        pedido = Caja.objects.create(**validated_data)
        for caja_data in cajas_data:
            Imagen.objects.create(caja=pedido, **caja_data)
        return pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['usuario','nombre','created_at','tipoPago','total']

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

    def to_representation(self, instance):
        data = super(DeliverySerializer, self).to_representation(instance)
        # Agrega info de cajas
        cajas = data.pop('cajas')
        query = Caja.objects.filter(id__in=cajas)
        data['cajas'] = CajaSerializer(query, many=True).data

        return data