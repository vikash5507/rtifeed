# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rtiapp', '0012_notification_read_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_relevance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relevance', models.FloatField(default=0.0)),
                ('views', models.IntegerField(default=0)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(to='rtiapp.Activity')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
