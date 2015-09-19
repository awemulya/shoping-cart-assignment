# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_remove_cart_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
