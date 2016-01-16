# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='hastags',
            field=models.CharField(default=b'a', max_length=123),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.CharField(default=b'a', max_length=128),
        ),
        migrations.AddField(
            model_name='article',
            name='noofslides',
            field=models.IntegerField(default=b'1'),
        ),
        migrations.AddField(
            model_name='article',
            name='reference',
            field=models.CharField(default=b'd', max_length=128),
        ),
    ]
