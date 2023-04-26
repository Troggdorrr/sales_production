from rest_framework import serializers

from products.models import PromoType


class PromoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoType
        fields = ["id", "name"]
