from django.contrib import admin
from models import BLEDevice, BLEData, Gateway


class BLEDeviceAdmin(admin.ModelAdmin):
    model = BLEDevice


class BLEDataAdmin(admin.ModelAdmin):
    model = BLEData


class BLEDeviceInlineAdmin (admin.TabularInline):
    model = BLEDevice


class GatewayAdmin(admin.ModelAdmin):
    model = Gateway
    inlines = [BLEDeviceInlineAdmin]



admin.site.register(BLEDevice, BLEDeviceAdmin)
admin.site.register(BLEData, BLEDataAdmin)
admin.site.register(Gateway, GatewayAdmin)