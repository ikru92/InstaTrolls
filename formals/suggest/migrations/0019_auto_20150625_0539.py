# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0018_auto_20150615_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentImg',
            field=models.FileField(upload_to=b'comment/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 5, 39, 12, 70022, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 5, 39, 12, 69183, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
