# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0014_auto_20150801_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 9, 3, 45, 352862, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.FileField(upload_to=b'post/', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 2, 9, 3, 45, 352061, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([]),
        ),
    ]
