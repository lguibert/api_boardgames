# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0003_boardgames_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgames',
            name='image',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
