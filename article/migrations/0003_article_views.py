# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160116_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=b'0'),
        ),
    ]
