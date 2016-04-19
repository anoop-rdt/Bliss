import datetime
import json
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route

from .models import BLEDevice
from .serializers import BLEDeviceSerializer


class BLEDeviceViewSet(viewsets.ModelViewSet):
    """
    API viewset for BLE device.
    """
    serializer_class = BLEDeviceSerializer
    queryset = BLEDevice.objects.all()
    permission_classes = (IsAuthenticated,)