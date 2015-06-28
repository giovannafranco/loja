# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_produto_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 6, 28, 4, 19, 21, 782156, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
