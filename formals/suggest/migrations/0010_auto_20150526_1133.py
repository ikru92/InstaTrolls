# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0009_auto_20150526_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentImg',
            field=models.FileField(default=None, upload_to=b'comment/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 11, 33, 30, 976291, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 11, 33, 30, 975485, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
