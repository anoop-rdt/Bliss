from django.db import models
from django.utils import timezone


class AbstractTimestampModel(models.Model):
    created_on = models.DateField(auto_now_add=True, editable=False)
    modified_on = models.DateField(auto_now=True, editable=False)

    class Meta:
        abstract = True

class Gateway(AbstractTimestampModel):
    title = models.CharField(max_length=256)
    source_lat = models.DecimalField(max_digits=8, decimal_places=3)
    source_long = models.DecimalField(max_digits=8, decimal_places=3)
    destination_lat = models.DecimalField(max_digits=8, decimal_places=3)
    destination_long = models.DecimalField(max_digits=8, decimal_places=3)
    current_lat = models.DecimalField(max_digits=8, decimal_places=3)
    current_lat = models.DecimalField(max_digits=8, decimal_places=3)

    def __unicode__(self):
        return str(self.title)


class BLEDevice(AbstractTimestampModel):
    name = models.CharField(max_length=256)
    ble_device_id = models.CharField(max_length=256, primary_key=True)
    gateway = models.ForeignKey(Gateway,related_name='devices')

    def __unicode__(self):
        return str(self.name)


class BLEData(AbstractTimestampModel):
    title = models.CharField(max_length=256)
    temperature = models.FloatField()
    device = models.ForeignKey(BLEDevice,related_name='data')

    def __unicode__(self):
        return str(self.title)
