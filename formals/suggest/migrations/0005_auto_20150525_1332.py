# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0004_auto_20150525_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 13, 32, 28, 681210, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.FileField(default=b'/home/akhilk/developer/python/formals/avatar/dp.png', upload_to=b'avatar/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 25, 13, 32, 28, 680559, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
