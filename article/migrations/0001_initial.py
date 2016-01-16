# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('category', models.CharField(default=b'a', max_length=35)),
                ('language', models.CharField(default=b'c', max_length=32)),
                ('title', models.CharField(default=b'q', max_length=128)),
                ('url', models.CharField(default=b'u', max_length=123)),
                ('keywords', models.CharField(default=b's', max_length=128)),
                ('content', models.TextField()),
                ('subheading', models.CharField(default=b'sh', max_length=80)),
            ],
        ),
    ]
