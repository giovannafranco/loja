# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0005_auto_20150628_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
