# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0007_activity_user_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(max_length=20, choices=[(b'rti_query', b'rti_query'), (b'rti_response', b'rti_response'), (b'comment', b'comment'), (b'like', b'like'), (b'follow', b'follow')]),
            preserve_default=True,
        ),
    ]
