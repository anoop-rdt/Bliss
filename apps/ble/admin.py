from django.contrib import admin
from models import BLEDevice, BLEData, Gateway, Company, RoomEnvironment
from actions import export_csv_action


class BLEDeviceAdmin(admin.ModelAdmin):
    model = BLEDevice
    actions = [
        export_csv_action("Export BLE Device Report",
            fields=[
                ('ble_device_id', 'BLE Device ID'),
                ('name', 'Name'),
                ('environment__max_temp', 'Max Temp'),
                ('environment__min_temp', 'Min Temp'),
                ('current_temp', 'Current Temperature'),
                ('current_humidity', 'Current Humidity'),
                ('gateway', 'Room'),
                ('created_on', 'Created On'),
            ],
            header=True
        ),
    ]


class BLEDataAdmin(admin.ModelAdmin):
    model = BLEData
    actions = [
        export_csv_action("Export BLE Device Report",
            fields=[
                ('device__ble_device_id', 'BLE Device ID'),
                ('device__name', 'Name'),
                ('device__gateway', 'Room'),
                ('temperature', 'Temperature'),
                ('humidity', 'Humidity'),
                ('created_on', 'Created On'),
            ],
            header=True
        ),
    ]

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