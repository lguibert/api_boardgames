# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0004_boardgames_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardgames',
            name='sub_name',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
