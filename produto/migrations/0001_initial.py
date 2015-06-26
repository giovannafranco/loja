# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.CharField(max_length=45)),
                ('imagem', models.FileField(upload_to=b'')),
                ('qtdEstoque', models.IntegerField()),
                ('valor', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
    ]
