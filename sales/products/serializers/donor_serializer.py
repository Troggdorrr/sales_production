from rest_framework import serializers

from products.models import Donor


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ["id", "name", "logo", "url"]
