# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_historicplace_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicplace',
            name='ref_num',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='historicplace',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
