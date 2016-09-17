# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_json_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='json_data',
        ),
        migrations.AddField(
            model_name='plan',
            name='json_data',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
