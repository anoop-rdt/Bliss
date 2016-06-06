import datetime
import json
from rest_framework import viewsets
from rest_framework.decorators import api_view,detail_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import list_route

from .models import BLEDevice, BLEData, Gateway, RoomEnvironment
from .serializers import BLEDeviceSerializer, BLEDataSerializer, GatewaySerializer
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Count


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
    API viewset for ble devices.
    """
    serializer_class = GatewaySerializer
    queryset = Gateway.objects.all()



class GatewayListView(ListView):
    model = Gateway

    def get_context_data(self, **kwargs):
        context = super(GatewayListView, self).get_context_data(**kwargs)
        total_tags = 0
        warning_tags_count  = len([device for device in BLEDevice.objects.all() if device.temp_status=='warning'])
        for gateway in self.object_list:
            gateway.status_wise_tags = gateway.devices.values('environment__temp_status').annotate(Count("ble_device_id"))
            total_tags += gateway.devices.count()
        context['total_tags'] = total_tags
        context['warning_tags_count'] = warning_tags_count
        return context

class GatewayDetailView(DetailView):
    model = Gateway

    def get_context_data(self, **kwargs):
        for each in self.object.devices.all():
            print each.temp_status
        context = super(GatewayDetailView, self).get_context_data(**kwargs)
        warning_tags_count  = len([device for device in self.object.devices.all() if device.temp_status=='warning'])
        room_envs = RoomEnvironment.objects.all()
        context['room_envs'] = room_envs
        context['warning_tags_count'] = warning_tags_count
        return context

class DeviceDetailView(DetailView):
    model = BLEDevice

    def get_context_data(self, **kwargs):
        context = kwargs
        data = []
        context['device'] = self.object
        for each_data in self.object.data.all():
            temp_data = {}
            temp_data['y'] = each_data.created_on.strftime("%Y-%m-%d %H:%M:%S")
            temp_data['temperature'] = each_data.temperature
            data.append(temp_data)
        context['data'] = json.dumps(data)
        return context


@login_required
def route_map(request, pk):
    gateway = Gateway.objects.get(id=pk)
    return render(request, 'ble/route_map.html', {'gateway':gateway})

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('gateways'))
    return render_to_response('ble/login.html', context_instance=RequestContext(request))