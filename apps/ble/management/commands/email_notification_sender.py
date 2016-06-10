# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from apps.ble.models import *


class Command(BaseCommand):
    help = "Send email notifications to Bliss admin"

    def __init__(self):
        super(Command, self).__init__()
        self.message = u'''{} in {} reached {}\xb0C '''

    def handle(self, *args, **options):
        for device in BLEDevice.objects.all():
            if device.temp_status in ('warning', 'danger'):
                try:
                    send_mail(device.temp_status, self.message.format(device,device.gateway,device.current_temp), settings.ADMIN_EMAIL, [device.gateway.company.email_address])
                except Exception,e:
                    print device,e



