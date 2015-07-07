# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0013_auto_20150801_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 1, 14, 25, 47, 876791, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lover',
            name='love_post',
            field=models.ForeignKey(related_name='love_post', to='suggest.Post'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lover',
            name='lover_user',
            field=models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 1, 14, 25, 47, 875997, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='lover',
            unique_together=set([('lover_user', 'love_post')]),
        ),
    ]
