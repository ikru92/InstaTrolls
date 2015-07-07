# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0017_auto_20150602_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='total_comment',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 5, 34, 45, 765646, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 5, 34, 45, 764834, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
