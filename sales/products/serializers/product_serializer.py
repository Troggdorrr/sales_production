from rest_framework import serializers

from products.models import Product

from .promo_serializer import PromoSerializer
from .donor_serializer import DonorSerializer


class ProductSerializer(serializers.ModelSerializer):
    promo = PromoSerializer(read_only=True)
    donor = DonorSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "poster",
            "price",
            "promo_price",
            "url",
            "promo",
            "donor",
        ]
