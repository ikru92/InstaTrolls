# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0016_auto_20150602_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 12, 38, 2, 812847, tzinfo=utc)),
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
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 12, 38, 2, 812047, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
