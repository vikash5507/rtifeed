# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0035_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='prority',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
