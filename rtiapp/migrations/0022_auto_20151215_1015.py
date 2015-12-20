# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0021_auto_20151215_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_link',
            field=models.ForeignKey(to='rtiapp.Activity', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.CharField(max_length=20, choices=[(b'rti_query', b'rti_query'), (b'rti_response', b'rti_response'), (b'comment', b'comment'), (b'like', b'like'), (b'follow', b'follow'), (b'spam', b'spam'), (b'comment_like', b'comment_like')]),
            preserve_default=True,
        ),
    ]
