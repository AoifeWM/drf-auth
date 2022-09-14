from rest_framework import serializers
from .models import Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        feilds = ('id', 'name', 'quantity', 'price_each', 'time', 'purchaser')
        model = Sale