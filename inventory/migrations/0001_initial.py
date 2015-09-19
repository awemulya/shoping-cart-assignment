# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('item_id', models.CharField(max_length=20)),
                ('merchant_id', models.CharField(max_length=20)),
                ('item_name', models.CharField(max_length=254)),
                ('item_price', models.FloatField(default=0.0)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('merchant_obj', models.ForeignKey(to='merchant.Merchant', related_name='items')),
            ],
        ),
    ]
