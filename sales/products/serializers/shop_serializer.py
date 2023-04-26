from rest_framework import serializers

from products.models import Shop

from .city_serializer import CitySerializer


class ShopSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Shop
        fields = ["id", "address", "city"]
