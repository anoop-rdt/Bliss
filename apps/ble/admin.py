from django.contrib import admin
from models import BLEDevice, BLEData, Gateway, Company, RoomEnvironment


class BLEDeviceAdmin(admin.ModelAdmin):
    model = BLEDevice


class BLEDataAdmin(admin.ModelAdmin):
    model = BLEData


class CompanyAdmin(admin.ModelAdmin):
    model = Company


class RoomEnvironmentAdmin(admin.ModelAdmin):
    model = RoomEnvironment


class BLEDeviceInlineAdmin (admin.TabularInline):
    model = BLEDevice


class GatewayAdmin(admin.ModelAdmin):
    model = Gateway
    inlines = [BLEDeviceInlineAdmin]



admin.site.register(BLEDevice, BLEDeviceAdmin)
admin.site.register(BLEData, BLEDataAdmin)
admin.site.register(Gateway, GatewayAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(RoomEnvironment, RoomEnvironmentAdmin)