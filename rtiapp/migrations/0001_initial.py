# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_line', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('pincode', models.CharField(max_length=200, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('entry_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Central_authority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authority_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Central_department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commment_text', models.TextField(null=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Follow_query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Follow_user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notification_text', models.CharField(max_length=200)),
                ('notification_url', models.CharField(max_length=300)),
                ('notification_type', models.CharField(max_length=200)),
                ('notification_status', models.BooleanField(default=False)),
                ('seen_date', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relevance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relevance', models.FloatField(default=0.0)),
                ('views', models.IntegerField(default=0)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RTI_query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query_text', models.TextField()),
                ('description', models.CharField(max_length=200)),
                ('rti_number', models.CharField(max_length=50)),
                ('rti_file_date', models.DateTimeField()),
                ('response_status', models.BooleanField(default=False)),
                ('query_type', models.CharField(max_length=50)),
                ('entry_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Central_RTI_query',
            fields=[
                ('rti_query', models.ForeignKey(primary_key=True, serialize=False, to='rtiapp.RTI_query')),
                ('authority', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='rtiapp.Central_authority', null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.SET_DEFAULT, default=1, to='rtiapp.Central_department')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RTI_response',
            fields=[
                ('rti_query', models.ForeignKey(primary_key=True, serialize=False, to='rtiapp.RTI_query')),
                ('response_text', models.TextField()),
                ('description', models.CharField(max_length=200)),
                ('rti_response_date', models.DateTimeField(null=True)),
                ('entry_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RTI_tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('share_text', models.TextField(null=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_name', models.CharField(max_length=200)),
                ('capital_name', models.CharField(max_length=200)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State_authority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authority_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State_department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department_name', models.CharField(max_length=200)),
                ('state', models.ForeignKey(to='rtiapp.State')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State_RTI_query',
            fields=[
                ('rti_query', models.ForeignKey(primary_key=True, serialize=False, to='rtiapp.RTI_query')),
                ('authority', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='rtiapp.State_authority', null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.SET_DEFAULT, default=1, to='rtiapp.State_department')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_text', models.CharField(max_length=200)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profilePicture', models.ImageField(default=b'static/profile_picture/default.jpg', upload_to=b'static/profile_picture')),
                ('reputation', models.FloatField(default=10)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('date_of_birth', models.DateTimeField(null=True)),
                ('bio_description', models.CharField(max_length=200)),
                ('entry_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(to='rtiapp.Address', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('tag', models.ForeignKey(to='rtiapp.Tag')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='state_authority',
            name='department',
            field=models.ForeignKey(to='rtiapp.State_department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='share',
            name='rti_query',
            field=models.ForeignKey(to='rtiapp.RTI_query'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='share',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rti_tag',
            name='rti_query',
            field=models.ForeignKey(to='rtiapp.RTI_query'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rti_tag',
            name='tag',
            field=models.ForeignKey(to='rtiapp.Tag'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rti_query',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relevance',
            name='rti_query',
            field=models.ForeignKey(to='rtiapp.RTI_query'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='relevance',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notification',
            name='other_user',
            field=models.ForeignKey(related_name='notified_by', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notification',
            name='rti_query',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='rtiapp.RTI_query', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(related_name='notified', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='rti_query',
            field=models.ForeignKey(to='rtiapp.RTI_query'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='follow_user',
            name='followee',
            field=models.ForeignKey(related_name='followee', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='follow_user',
            name='follower',
            field=models.ForeignKey(related_name='follower', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='follow_query',
            name='rti_query',
            field=models.ForeignKey(to='rtiapp.RTI_query'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='follow_query',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='rti_query',
            field=models.ForeignKey(to='rtiapp.RTI_query'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='central_authority',
            name='department',
            field=models.ForeignKey(to='rtiapp.Central_department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='rtiapp.State', null=True),
            preserve_default=True,
        ),
    ]
