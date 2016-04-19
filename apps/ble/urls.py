from rest_framework_nested import routers
from django.conf.urls import patterns, include, url
from views import BLEDeviceViewSet

router = routers.SimpleRouter()
router.register('ble-device', BLEDeviceViewSet, base_name='ble-device')

urlpatterns = patterns(
    '',
    url(r'api/', include(router.urls)),
)