# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0003_auto_20150628_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrinho',
            name='compra',
            field=models.OneToOneField(related_name='carrinho', null=True, to='carrinho.Compra'),
        ),
    ]
