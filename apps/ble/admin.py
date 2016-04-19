from django.contrib import admin
from models import BLEDevice


class BLEDeviceAdmin(admin.ModelAdmin):
    model = BLEDevice

    
admin.site.register(BLEDevice, BLEDeviceAdmin)