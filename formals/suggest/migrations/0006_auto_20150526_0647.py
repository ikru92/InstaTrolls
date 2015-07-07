# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0005_auto_20150525_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentImg',
            field=models.FileField(default=None, upload_to=b'comment/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 6, 47, 16, 650754, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.FileField(default=b'avatar/dp.png', upload_to=b'avatar/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 6, 47, 16, 649942, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
