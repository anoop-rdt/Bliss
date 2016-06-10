# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from django.conf import settings
from apps.ble.models import *


class Command(BaseCommand):
    help = "Send sms notifications to Bliss admin"

    def __init__(self):
        super(Command, self).__init__()
        self.temperature_unit = '℃'
        self.client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        self.message = u'''{}:{} in {}.Current:{}\xb0C '''

    def handle(self, *args, **options):
        for device in BLEDevice.objects.all():
            if device.temp_status in ('warning', 'danger'):
                try:
                    message = self.client.messages.create(body=self.message.format(device.temp_status,device.gateway,device,round(device.current_temp,1))\
                        ,to=device.gateway.company.phone_number,from_=settings.TWILIO_FROM_NUMBER)
                except TwilioRestException as e:
                    print device,e



