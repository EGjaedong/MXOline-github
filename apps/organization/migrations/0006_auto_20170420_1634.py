# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-20 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default=b'', upload_to=b'/%Y/%m', verbose_name='\u5934\u50cf'),
        ),
    ]
