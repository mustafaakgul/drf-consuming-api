from rest_framework import serializers
from .models import SavedEmbeds, CartItem


class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedEmbeds


class CartItemSerializer(serializers.ModelSerializer):
    """
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)
    """

    class Meta:
        model = CartItem
        fields = ('__all__')