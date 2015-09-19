# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_transaction_transaction_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='transaction_obj',
            field=models.ForeignKey(to='sales.Transaction', related_name='sales'),
        ),
    ]
