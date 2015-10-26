# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0004_auto_20151022_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rti_query_file',
            name='query_document',
            field=models.FileField(null=True, upload_to=b'query_docs'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rti_query_file',
            name='query_picture',
            field=models.ImageField(default=b'query_pictures/default.jpg', upload_to=b'query_pictures'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rti_response_file',
            name='query_document',
            field=models.FileField(null=True, upload_to=b'response_documents'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rti_response_file',
            name='query_picture',
            field=models.ImageField(default=b'response_pictures/default.jpg', upload_to=b'response_pictures'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='profile_picture',
            field=models.ImageField(default=b'profile_pictures/default.jpg', upload_to=b'profile_pictures'),
            preserve_default=True,
        ),
    ]
