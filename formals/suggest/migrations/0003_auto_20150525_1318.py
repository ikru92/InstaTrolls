# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0002_auto_20150525_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='avatar',
            field=models.FileField(default=b'avatar/dp.png', upload_to=b'avatar/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 13, 18, 26, 818579, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.FileField(upload_to=b'post/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 13, 18, 26, 817790, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
