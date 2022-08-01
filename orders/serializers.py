from rest_framework import serializers
from .models import *


class OrdersSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(default=serializers.user.id)
    class Meta:
        model = Orders
        fields = '__all__'