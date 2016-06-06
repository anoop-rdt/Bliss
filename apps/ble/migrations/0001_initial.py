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
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BLEDevice',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
                ('ble_device_id', models.CharField(max_length=256, serialize=False, primary_key=True)),
                ('current_temp', models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)),
                ('current_humidity', models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=2000, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('room', models.CharField(max_length=256, null=True, blank=True)),
                ('company', models.ForeignKey(related_name='gateways', to='ble.Company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomEnvironment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temp_status', models.CharField(max_length=256, null=True, blank=True)),
                ('max_temp', models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)),
                ('min_temp', models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)),
                ('humid_status', models.CharField(max_length=256, null=True, blank=True)),
                ('max_humidity', models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)),
                ('min_humidity', models.DecimalField(null=True, max_digits=8, decimal_places=3, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='bledevice',
            name='environment',
            field=models.ForeignKey(related_name='devices', to='ble.RoomEnvironment'),
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
