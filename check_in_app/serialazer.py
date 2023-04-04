from abc import ABCMeta
import json
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import serializers
from .models import *


class ResidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resident
        fields = "__all__"


class ResidentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = "__all__"


class TransportTypeSer(serializers.ModelSerializer):
    class Meta:
        model = TransportType
        fields = "__all__"


class TransportSer(serializers.ModelSerializer):
    type = TransportTypeSer(many=False)

    class Meta:
        model = Transport
        fields = "__all__"


class OrderSer(serializers.ModelSerializer):
    user_id = ResidentSerializer(many=False)
    transport_id = TransportSer(many=False)

    class Meta:
        model = Order
        fields = "__all__"


class OrderFilterSer(serializers.ModelSerializer):
    user_id_id = ResidentSerializer(many=True)
    transport_id_id = TransportSer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'time_end', 'order_name', 'time_start', 'transport_id_id', 'user_id_id']


class TransportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
