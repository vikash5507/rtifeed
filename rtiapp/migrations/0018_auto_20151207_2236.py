# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0017_remove_rti_response_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rti_response_file',
            old_name='query_document',
            new_name='response_document',
        ),
        migrations.RenameField(
            model_name='rti_response_file',
            old_name='query_picture',
            new_name='response_picture',
        ),
    ]
