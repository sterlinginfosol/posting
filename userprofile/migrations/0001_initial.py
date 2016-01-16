# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(default=b'a', max_length=128)),
                ('password', models.CharField(default=b'b', max_length=128)),
                ('emailid', models.CharField(default=b'c', max_length=128)),
                ('group', models.CharField(default=b'd', max_length=34)),
            ],
        ),
    ]
