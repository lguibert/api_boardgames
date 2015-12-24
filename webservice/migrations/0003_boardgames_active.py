# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0002_auto_20151213_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgames',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
