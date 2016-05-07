# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ble', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bledevice',
            name='max_temp',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='bledevice',
            name='min_temp',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='max_temp',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='min_temp',
            field=models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True),
        ),
    ]
