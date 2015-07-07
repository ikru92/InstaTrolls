# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0006_auto_20150526_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_by',
            field=models.ForeignKey(related_name='commented_by', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 7, 53, 32, 329477, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(related_name='posted_by', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 7, 53, 32, 328678, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
