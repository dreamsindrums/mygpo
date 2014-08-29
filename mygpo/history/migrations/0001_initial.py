# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_syncgroup_protect'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('podcasts', '0023_auto_20140729_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField()),
                ('action', models.CharField(max_length=11, choices=[(b'subscribe', b'subscribed'), (b'unsubscribe', b'unsubscribed')])),
                ('client', models.ForeignKey(to='users.Client')),
                ('podcast', models.ForeignKey(to='podcasts.Podcast')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': [b'timestamp'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='historyentry',
            index_together=set([(b'user', b'podcast'), (b'user', b'client')]),
        ),
    ]