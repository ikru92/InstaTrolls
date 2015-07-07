# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('suggest', '0010_auto_20150526_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lover',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('love_post', models.ForeignKey(related_name='love_post', to='suggest.Post')),
                ('lover_user', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='post',
            old_name='vote',
            new_name='love',
        ),
        migrations.AlterField(
            model_name='comment',
            name='commented_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 1, 14, 9, 17, 209231, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 1, 14, 9, 17, 208440, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
