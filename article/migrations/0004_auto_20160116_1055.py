# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_article_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='dateTime',
            field=models.IntegerField(default=b'2016'),
        ),
        migrations.AddField(
            model_name='article',
            name='postedby',
            field=models.CharField(default=b'shefali', max_length=128),
        ),
    ]
