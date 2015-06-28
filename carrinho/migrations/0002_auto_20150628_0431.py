# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='valor',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
    ]
