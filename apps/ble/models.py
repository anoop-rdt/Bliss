from django.db import models
from django.utils import timezone


class AbstractTimestampModel(models.Model):
    created_on = models.DateField(auto_now_add=True, editable=False)
    modified_on = models.DateField(auto_now=True, editable=False)

    class Meta:
        abstract = True



class AbstractConditionsModel(models.Model):
    """Common conditions for gateway and ble_device"""
    FROZEN = 0
    CHILLED = 1
    COOL = 2
    AMBIENT = 3
    STATUS_CHOICES = (
        (FROZEN, 'Frozen'),
        (CHILLED, 'Chilled'),
        (COOL, 'Cool'),
        (AMBIENT, 'Ambient'),
    )
    max_temp = models.DecimalField(max_digits=8, decimal_places=3,null=True, blank=True)
    min_temp = models.DecimalField(max_digits=8, decimal_places=3,null=True, blank=True)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES) 
    class Meta:
        abstract = True

        

class Gateway(AbstractTimestampModel,AbstractConditionsModel):
    title = models.CharField(max_length=256)
    source_lat = models.DecimalField(max_digits=8, decimal_places=3)
    source_long = models.DecimalField(max_digits=8, decimal_places=3)
    destination_lat = models.DecimalField(max_digits=8, decimal_places=3)
    destination_long = models.DecimalField(max_digits=8, decimal_places=3)
    current_lat = models.DecimalField(max_digits=8, decimal_places=3)
    current_long = models.DecimalField(max_digits=8, decimal_places=3)

    def __unicode__(self):
        return str(self.title)


class BLEDevice(AbstractTimestampModel,AbstractConditionsModel):
    name = models.CharField(max_length=256)
    ble_device_id = models.CharField(max_length=256, primary_key=True)
    gateway = models.ForeignKey(Gateway,related_name='devices')
    current_temp = models.DecimalField(max_digits=8, decimal_places=3)
    def __unicode__(self):
        return str(self.name)


class BLEData(AbstractTimestampModel):
    temperature = models.FloatField()
    device = models.ForeignKey(BLEDevice,related_name='data')

    def __unicode__(self):
        return str(self.title)
