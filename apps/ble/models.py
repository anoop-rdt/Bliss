from django.db import models
from django.utils import timezone
from django.conf import settings

class AbstractTimestampModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=True)
    modified_on = models.DateTimeField(auto_now=True, editable=True)

    class Meta:
        abstract = True

class Company(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=2000, null=True, blank=True)

    def __unicode__(self):
        return str(self.title)

class RoomEnvironment(models.Model):
    """Common conditions for  ble_device"""
    temp_status = models.CharField(max_length=256,null=True, blank=True)
    max_temp = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    min_temp = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    humid_status = models.CharField(max_length=256,null=True, blank=True)
    max_humidity = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    min_humidity = models.DecimalField(max_digits=8, decimal_places=3, null=True, blank=True)
    
    def __unicode__(self):
        return str(self.temp_status + '-' + self.humid_status)         

class Gateway(AbstractTimestampModel):
    title = models.CharField(max_length=256)
    room = models.CharField(max_length=256,null=True, blank=True)
    company = models.ForeignKey(Company, related_name='gateways')

    def __unicode__(self):
        return str(self.title)


class BLEDevice(AbstractTimestampModel):
    name = models.CharField(max_length=256)
    ble_device_id = models.CharField(max_length=256, primary_key=True)
    environment = models.ForeignKey(RoomEnvironment,related_name='devices')
    gateway = models.ForeignKey(Gateway,related_name='devices')
    current_temp = models.DecimalField(max_digits=8, decimal_places=3,null=True, blank=True)
    current_humidity = models.DecimalField(max_digits=8, decimal_places=3,null=True, blank=True)
    
    def __unicode__(self):
        return str(self.name)

    @property
    def temp_status(self):
        max_temp_diff = self.environment.max_temp - self.current_temp
        min_temp_diff = self.current_temp - self.environment.min_temp
        temp_in_danger = self.environment.max_temp <= self.current_temp <= self.environment.min_temp
        humid_in_danger = False
        max_humid_diff = min_humid_diff = (settings.WARNING_MODE_DIFFERENCE + 1)
        if self.environment.max_humidity and self.current_humidity and self.environment.min_humidity:
            max_humid_diff = self.environment.max_humidity - self.current_humidity
            min_humid_diff = self.current_humidity - self.environment.min_humidity
            humid_in_danger = self.environment.max_humidity <= self.current_humidity <= self.environment.min_humidity
        if temp_in_danger or humid_in_danger:
            return "danger"
        elif any(abs(x)<=settings.WARNING_MODE_DIFFERENCE for x in (max_temp_diff, min_temp_diff, max_humid_diff, min_humid_diff)):
            return "warning"
        else:
            return "success"

class BLEData(AbstractTimestampModel):
    temperature = models.FloatField()
    humidity = models.FloatField()
    device = models.ForeignKey(BLEDevice,related_name='data')

    def __unicode__(self):
        return str(self.device.name)

    def save(self, *args, **kwargs):
        self.device.current_temp = self.temperature
        self.device.current_humidity = self.humidity
        self.device.save()
        super(BLEData, self).save(*args, **kwargs)