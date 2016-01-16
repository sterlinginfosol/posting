# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_article_postedby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='dateTime',
            field=models.DateField(),
        ),
    ]
