# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('client', models.CharField(default=b'a', max_length=128)),
                ('formate', models.IntegerField(default=b'1')),
                ('slot', models.IntegerField(default=b'909012')),
                ('page', models.CharField(default=b'article', max_length=b'40')),
                ('width', models.IntegerField(default=b'100')),
                ('height', models.IntegerField(default=b'100')),
                ('min_width', models.IntegerField(default=b'90')),
                ('min_height', models.IntegerField(default=b'90')),
                ('display', models.CharField(default=b'', max_length=67)),
                ('published', models.IntegerField(default=b'1')),
            ],
        ),
    ]
