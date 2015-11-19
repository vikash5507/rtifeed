# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rtiapp', '0006_relevance_feed_head_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity_type', models.CharField(max_length=20, choices=[(b'comment', b'comment'), (b'like', b'like'), (b'follow', b'follow')])),
                ('meta_data', models.TextField()),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('rti_query', models.ForeignKey(to='rtiapp.RTI_query')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relevance', models.FloatField(default=0.0)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(to='rtiapp.Activity')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
