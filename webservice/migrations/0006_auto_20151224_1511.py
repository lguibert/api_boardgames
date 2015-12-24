# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0005_boardgames_sub_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardgames',
            name='date_buy',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='boardgames',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='boardgames',
            name='image',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='boardgames',
            name='price',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='boardgames',
            name='sub_name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
