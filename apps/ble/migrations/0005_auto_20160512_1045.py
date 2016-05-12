# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ble', '0004_auto_20160509_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bledata',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bledata',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='bledevice',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='bledevice',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
