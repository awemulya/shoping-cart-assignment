# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_cart_rows'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
