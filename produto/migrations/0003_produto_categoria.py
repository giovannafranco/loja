# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20150628_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default=1, to='produto.Categoria'),
            preserve_default=False,
        ),
    ]
