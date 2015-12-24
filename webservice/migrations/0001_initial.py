# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boardgames',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('date_buy', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('description', models.TextField()),
                ('max_player', models.IntegerField()),
                ('min_player', models.IntegerField()),
                ('extension', models.ForeignKey(to='webservice.Boardgames')),
            ],
        ),
    ]
