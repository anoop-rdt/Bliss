import datetime
import json

from django.db.models import Q
from django.utils import timezone

from rest_framework import serializers
from models import BLEDevice, BLEData, Gateway


class BLEDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = BLEDevice


class BLEDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = BLEData


class GatewaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Gateway