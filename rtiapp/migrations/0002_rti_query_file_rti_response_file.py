# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RTI_query_file',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query_picture', models.ImageField(default=b'static/query_picture/default.jpg', upload_to=b'static/query_picture')),
                ('query_document', models.FileField(null=True, upload_to=b'static/query_document')),
                ('rti_query', models.ForeignKey(to='rtiapp.RTI_query')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RTI_response_file',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query_picture', models.ImageField(default=b'static/response_picture/default.jpg', upload_to=b'static/response_picture')),
                ('query_document', models.FileField(null=True, upload_to=b'static/response_document')),
                ('rti_response', models.ForeignKey(to='rtiapp.RTI_response')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
