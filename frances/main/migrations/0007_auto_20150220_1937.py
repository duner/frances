# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150216_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicplace',
            name='address',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historicplace',
            name='city',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historicplace',
            name='county',
            field=models.CharField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historicplace',
            name='date_listed',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historicplace',
            name='wikipedia_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
