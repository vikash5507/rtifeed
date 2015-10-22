# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='profilePicture',
            new_name='profile_picture',
        ),
        migrations.AlterField(
            model_name='state',
            name='capital_name',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
