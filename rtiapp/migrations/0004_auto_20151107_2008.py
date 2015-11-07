# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rtiapp', '0003_useractivity'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity_type', models.CharField(max_length=50, choices=[(b'comment_rti', b'comment_rti'), (b'like_rti', b'like_rti'), (b'follow_rti', b'follow_rti'), (b'edit_comment_rti', b'edit_comment_rti'), (b'delete_comment_rti', b'delete_comment_rti'), (b'unlike_rti', b'unlike_rti'), (b'unfollow_rti', b'unfollow_rti'), (b'follow_user', b'unfollow_user')])),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='useractivity',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserActivity',
        ),
    ]
