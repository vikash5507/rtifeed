# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0037_auto_20160107_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_picture',
            field=models.ImageField(null=True, upload_to=b'blog_pictures'),
            preserve_default=True,
        ),
    ]
