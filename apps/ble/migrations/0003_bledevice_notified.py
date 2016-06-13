# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ble', '0002_auto_20160610_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='bledevice',
            name='notified',
            field=models.BooleanField(default=False),
        ),
    ]
