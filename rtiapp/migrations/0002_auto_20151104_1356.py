# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rtiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow_department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('followee', models.ForeignKey(related_name='department_followee', to='rtiapp.Department')),
                ('follower', models.ForeignKey(related_name='department_follower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Follow_state',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('followee', models.ForeignKey(related_name='state_followee', to='rtiapp.State')),
                ('follower', models.ForeignKey(related_name='state_follower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Follow_topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('followee', models.ForeignKey(related_name='topic_followee', to='rtiapp.Tag')),
                ('follower', models.ForeignKey(related_name='topic_follower', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='follow_user',
            name='followee',
            field=models.ForeignKey(related_name='user_followee', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='follow_user',
            name='follower',
            field=models.ForeignKey(related_name='user_follower', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
