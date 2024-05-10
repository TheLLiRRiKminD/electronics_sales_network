from rest_framework import serializers
from .models import NetworkMember, Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.
    """

    class Meta:
        model = Product
        fields = '__all__'


class NetworkMemberSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели NetworkMember.
    """
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = NetworkMember
        fields = '__all__'
        read_only_fields = ('debt',)

    def validate(self, data):
        if data.get('supplier') and data['supplier'].hierarchy_level >= data.get('hierarchy_level', 0):
            raise serializers.ValidationError("Поставщик должен быть на более высоком уровне иерархии.")
        return data
