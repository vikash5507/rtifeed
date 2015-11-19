# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0008_auto_20151109_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='rti_query',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RemoveField(
            model_name='follow_query',
            name='rti_query',
        ),
        migrations.RemoveField(
            model_name='follow_query',
            name='user',
        ),
        migrations.DeleteModel(
            name='Follow_query',
        ),
        migrations.RemoveField(
            model_name='like',
            name='rti_query',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.RemoveField(
            model_name='share',
            name='rti_query',
        ),
        migrations.RemoveField(
            model_name='share',
            name='user',
        ),
        migrations.DeleteModel(
            name='Share',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='activity_id',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='notification_status',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='notification_text',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='notification_url',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='other_user',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='rti_query',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='seen_date',
        ),
        migrations.AddField(
            model_name='notification',
            name='activity',
            field=models.ForeignKey(to='rtiapp.Activity', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notification',
            name='follow',
            field=models.ForeignKey(to='rtiapp.Follow_user', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(max_length=20, choices=[(b'user_follow', b'user_follow'), (b'rti_query', b'rti_query')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
