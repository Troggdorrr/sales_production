from rest_framework import serializers

from products.models import Promo

from .promo_type_serializer import PromoTypeSerializer


class PromoSerializer(serializers.ModelSerializer):
    type = PromoTypeSerializer(read_only=True)

    class Meta:
        model = Promo
        fields = ["id", "date_begin", "date_end", "type"]
