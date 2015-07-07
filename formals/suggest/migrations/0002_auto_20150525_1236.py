# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commented_on', models.DateTimeField(default=datetime.datetime(2015, 5, 25, 12, 36, 14, 261351, tzinfo=utc))),
                ('comment', models.TextField(max_length=1000)),
                ('commented_by', models.ForeignKey(related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-commented_on'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posted_on', models.DateTimeField(default=datetime.datetime(2015, 5, 25, 12, 36, 14, 260553, tzinfo=utc))),
                ('description', models.TextField(max_length=1000)),
                ('vote', models.IntegerField(default=0)),
                ('post', models.FileField(upload_to=b'images/')),
                ('posted_by', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-posted_on'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='suggest.Post'),
            preserve_default=True,
        ),
    ]
