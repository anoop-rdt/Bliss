import datetime
import json
from rest_framework import viewsets
from rest_framework.decorators import api_view,detail_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route

from .models import BLEDevice, BLEData, Gateway
from .serializers import BLEDeviceSerializer, BLEDataSerializer, GatewaySerializer
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render



class BLEDeviceViewSet(viewsets.ModelViewSet):
    """
    API viewset for BLE device.
    """
    serializer_class = BLEDeviceSerializer
    queryset = BLEDevice.objects.all()


class BLEDataViewSet(viewsets.ModelViewSet):
    """
    API viewset for BLE device data.
    """
    serializer_class = BLEDataSerializer
    queryset = BLEData.objects.all()


class GatewaySerializerViewSet(viewsets.ModelViewSet):
    """
    API viewset for listing devices in prefered Category.
    """
    serializer_class = GatewaySerializer
    queryset = Gateway.objects.all()


class GatewayListView(ListView):

    model = Gateway


class GatewayDetailView(DetailView):

    model = Gateway


def route_map(request, pk):
    gateway = Gateway.objects.get(id=pk)
    return render(request, 'ble/route_map.html', {'gateway':gateway})
