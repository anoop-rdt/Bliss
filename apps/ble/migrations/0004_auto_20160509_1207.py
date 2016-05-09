# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ble', '0003_remove_bledata_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bledevice',
            name='current_temp',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True),
        ),
    ]
