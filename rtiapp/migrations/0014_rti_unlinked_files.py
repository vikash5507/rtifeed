# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0013_activity_relevance'),
    ]

    operations = [
        migrations.CreateModel(
            name='RTI_unlinked_files',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rti_hash', models.CharField(max_length=200)),
                ('query_picture', models.ImageField(upload_to=b'query_pictures')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
