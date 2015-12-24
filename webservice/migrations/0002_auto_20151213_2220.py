# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgames',
            name='extension',
            field=models.ForeignKey(to='webservice.Boardgames', null=True),
        ),
    ]
