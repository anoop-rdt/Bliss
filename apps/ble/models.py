from django.db import models
from django.utils import timezone


class BLEDevice(models.Model):
    name = models.CharField(max_length=256)
    ble_device_id = models.CharField(max_length=256, primary_key=True)
    registered_on = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=300)

    def __unicode__(self):
        return str(self.name)
