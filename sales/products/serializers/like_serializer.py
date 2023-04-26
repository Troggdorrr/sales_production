from rest_framework import serializers

from products.models import Like
from products.services.CRUD import LikeCRUD

from .product_serializer import ProductSerializer


class LikeSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    def create(self, validated_data) -> Like:
        return LikeCRUD.create(
            self.context["request"].user, self.context["view"].kwargs.get("product_pk")
        )

    class Meta:
        model = Like
        fields = ["user_id", "product", "created_at"]
