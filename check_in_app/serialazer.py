from abc import ABCMeta
import json
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class OrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizatoin
        fields = "__all__"


class ResidentSerializer(serializers.ModelSerializer):
    organization_id = OrgSerializer(many=False)

    class Meta:
        model = Resident
        fields = "__all__"


class HostelSerializers(serializers.ModelSerializer):
    address_id = AddressSerializer(many=False)

    class Meta:
        model = Hostel
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    hostel_id = HostelSerializers(many=False)

    class Meta:
        model = Room
        fields = "__all__"


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class CheckInSerializer(serializers.ModelSerializer):
    resident_id = ResidentSerializer(many=False)
    room_id = RoomSerializer(many=False)

    class Meta:
        model = Check_in_out
        fields = "__all__"


class CheckinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check_in_out
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    check_in_out_id = CheckInSerializer(many=False)

    class Meta:
        model = Payment
        fields = "__all__"


class ResidentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = "__all__"


class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
# class PaymentCreateSerializer(serializers.Serializer):
#     amount = serializers.FloatField(validators=[MinValueValidator(0)])
#     status = serializers.CharField(max_length=50)
#     date_pay = serializers.DateField(default=date.today)
#     check_in_out_id = models.ForeignKey(Check_in_out, on_delete=models.CASCADE, default=1)
#
#     def create(self, validated_data):
#         return Payment(**validated_data)


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
