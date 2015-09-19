# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('sr_no', models.IntegerField(default=0)),
                ('transaction_id', models.CharField(max_length=100)),
                ('item_id', models.CharField(max_length=100)),
                ('item_obj', models.ForeignKey(to='inventory.Item', related_name='sales')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField(null=True)),
                ('transaction_id', models.CharField(max_length=50)),
                ('customer_id', models.CharField(max_length=50)),
                ('cancel_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='sales',
            name='transaction_obj',
            field=models.ForeignKey(to='sales.Transaction'),
        ),
    ]
