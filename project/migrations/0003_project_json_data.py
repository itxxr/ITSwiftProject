# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_task_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='json_data',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
