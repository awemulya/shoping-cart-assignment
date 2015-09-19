# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_remove_transaction_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_timestamp',
            field=models.DateField(null=True),
        ),
    ]
