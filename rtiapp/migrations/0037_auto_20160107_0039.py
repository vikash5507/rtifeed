# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0036_faq_prority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='prority',
            new_name='priority',
        ),
    ]
