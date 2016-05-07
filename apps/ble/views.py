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
from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect


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

    def get_queryset(self):
        try:
            name = self.request.GET['name']
        except:
            name = ''
        if (name != ''):
            object_list = self.model.objects.filter(title__icontains = name)
        else:
            object_list = self.model.objects.all()
        return object_list


class GatewayDetailView(DetailView):
    model = Gateway


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