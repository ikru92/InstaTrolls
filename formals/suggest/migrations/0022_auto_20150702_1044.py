# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0021_auto_20150625_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=1000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentImg',
            field=models.FileField(upload_to=b'comment/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 10, 44, 22, 297397, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 2, 10, 44, 22, 296570, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
