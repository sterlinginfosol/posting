# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
        ('article', '0007_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='postedby',
            field=models.ForeignKey(default=b'1', to='userprofile.UserProfile'),
        ),
    ]
