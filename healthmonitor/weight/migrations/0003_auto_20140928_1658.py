# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0002_auto_20140928_1032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weight',
            options={'ordering': ['-date']},
        ),
    ]
