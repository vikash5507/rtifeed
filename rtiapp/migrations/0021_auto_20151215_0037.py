# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0020_email_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email_user',
            name='id',
        ),
        migrations.AddField(
            model_name='email_user',
            name='verification_code',
            field=models.CharField(default='12', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='email_user',
            name='verified',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='email_user',
            name='email',
            field=models.CharField(default='1@1.com', max_length=200, serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='email_user',
            name='first_name',
            field=models.CharField(default='p', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='email_user',
            name='last_name',
            field=models.CharField(default='p', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='email_user',
            name='password',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
    ]
