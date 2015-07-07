# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0008_auto_20150526_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 9, 43, 9, 12111, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='commentedOn', to='suggest.Post'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 9, 43, 9, 11307, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('commented_by', 'comment')]),
        ),
    ]
