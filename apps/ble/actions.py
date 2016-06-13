import csv
from django.http import HttpResponse
from django.core.mail import send_mail
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from django.conf import settings
from models import *

 
def prep_field(obj, field):
    """ Returns the field as a unicode string. If the field is a callable, it
    attempts to call it first, without arguments.
    """
    if '__' in field:
        bits = field.split('__')
        field = bits.pop()
 
        for bit in bits:
            obj = getattr(obj, bit, None)
 
            if obj is None:
                return ""
 
    attr = getattr(obj, field)
    output = attr() if callable(attr) else attr
    return unicode(output).encode('utf-8') if output else ""
 
 
def export_csv_action(description="Export as CSV", fields=None, exclude=None, header=True):
    """ This function returns an export csv action. """
    def export_as_csv(modeladmin, request, queryset):
        """ Generic csv export admin action.
        """
        opts = modeladmin.model._meta
        field_names = [field.name for field in opts.fields]
        labels = []
 
        if exclude:
            field_names = [f for f in field_names if f not in exclude]
 
        elif fields:
            field_names = [field for field, _ in fields]
            labels = [label for _, label in fields]
 
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % (
                unicode(opts).replace('.', '_')
            )
 
        writer = csv.writer(response)
 
        if header:
            writer.writerow(labels if labels else field_names)
        for obj in queryset:
            writer.writerow([prep_field(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = description
    return export_as_csv


def send_notification(email_message, email_subject, mail_to, sms_message,sms_to):
    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(body=sms_message,to=sms_to,from_=settings.TWILIO_FROM_NUMBER)
        send_mail(email_subject, email_message, settings.ADMIN_EMAIL,[mail_to])
    except Exception,e:
        print e
    return False

