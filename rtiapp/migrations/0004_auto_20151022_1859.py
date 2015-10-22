# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0003_central_department_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commment_text',
            new_name='comment_text',
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='bio_description',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
