# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BLEData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('temperature', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BLEDevice',
            fields=[
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('max_temp', models.DecimalField(max_digits=8, decimal_places=3)),
                ('min_temp', models.DecimalField(max_digits=8, decimal_places=3)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Frozen'), (1, b'Chilled'), (2, b'Cool'), (3, b'Ambient')])),
                ('name', models.CharField(max_length=256)),
                ('ble_device_id', models.CharField(max_length=256, serialize=False, primary_key=True)),
                ('current_temp', models.DecimalField(max_digits=8, decimal_places=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('modified_on', models.DateField(auto_now=True)),
                ('max_temp', models.DecimalField(max_digits=8, decimal_places=3)),
                ('min_temp', models.DecimalField(max_digits=8, decimal_places=3)),
                ('status', models.IntegerField(default=0, choices=[(0, b'Frozen'), (1, b'Chilled'), (2, b'Cool'), (3, b'Ambient')])),
                ('title', models.CharField(max_length=256)),
                ('source_lat', models.DecimalField(max_digits=8, decimal_places=3)),
                ('source_long', models.DecimalField(max_digits=8, decimal_places=3)),
                ('destination_lat', models.DecimalField(max_digits=8, decimal_places=3)),
                ('destination_long', models.DecimalField(max_digits=8, decimal_places=3)),
                ('current_lat', models.DecimalField(max_digits=8, decimal_places=3)),
                ('current_long', models.DecimalField(max_digits=8, decimal_places=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='bledevice',
            name='gateway',
            field=models.ForeignKey(related_name='devices', to='ble.Gateway'),
        ),
        migrations.AddField(
            model_name='bledata',
            name='device',
            field=models.ForeignKey(related_name='data', to='ble.BLEDevice'),
        ),
    ]
