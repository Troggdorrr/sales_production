from rest_framework import serializers

from .product_serializer import ProductSerializer


class AuthProductSerializer(ProductSerializer):
    is_liked = serializers.BooleanField(read_only=True)

    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ["is_liked"]