# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0003_auto_20141105_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='list',
        ),
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, to='lists.List'),
        ),
    ]
