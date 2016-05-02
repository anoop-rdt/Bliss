"""rdt_base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.conf import settings
from django.contrib import admin
from rest_framework_nested import routers
from apps.ble.views import BLEDeviceViewSet, GatewayListView, GatewayDetailView

router = routers.SimpleRouter()
router.register('ble-device', BLEDeviceViewSet, base_name='ble-device')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', GatewayListView.as_view(), name='gateways'),
	url(r'^gateway/(?P<pk>[\w._-]+)/$', GatewayDetailView.as_view(), name='gateway-detail'),
	url(r'^gateway-route/(?P<pk>[\w._-]+)/$', 'apps.ble.views.route_map', name='gateway-map'),
    # url(r'^temperature-graph/(?P<pk>[\w._-]+)/$', 'apps.ble.views.temp_graph_plot', name="data-graph"),
    url(r'api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views', url(r'^static/(?P<path>.*)', 'serve'))
