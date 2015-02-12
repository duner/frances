# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_historicplace_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicplace',
            name='name',
            field=models.CharField(max_length=250),
            preserve_default=True,
        ),
    ]
