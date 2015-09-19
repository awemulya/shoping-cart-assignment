# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('merchant_id', models.CharField(max_length=20)),
                ('merchant_name', models.CharField(max_length=100)),
                ('merchant_address', models.CharField(max_length=254)),
            ],
        ),
    ]
