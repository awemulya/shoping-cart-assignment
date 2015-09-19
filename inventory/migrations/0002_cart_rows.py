# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField()),
                ('status', models.FloatField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rows',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('sn', models.IntegerField(default=0)),
                ('quantity', models.FloatField(default=0.0)),
                ('unit', models.CharField(max_length=50)),
                ('cart', models.ForeignKey(to='inventory.Cart', related_name='rows')),
                ('item', models.ForeignKey(to='inventory.Item')),
            ],
        ),
    ]
