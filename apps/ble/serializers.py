import datetime
import json

from django.db.models import Q
from django.utils import timezone

from rest_framework import serializers
from models import BLEDevice


class BLEDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = BLEDevice