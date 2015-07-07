# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0007_auto_20150526_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_by',
            field=models.ForeignKey(related_name='commentedBy', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 7, 54, 38, 491029, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(related_name='postedBy', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 7, 54, 38, 490201, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
