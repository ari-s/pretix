# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0002_auto_20160209_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpermission',
            name='can_change_vouchers',
            field=models.BooleanField(default=True, verbose_name='Can change vouchers'),
        ),
    ]