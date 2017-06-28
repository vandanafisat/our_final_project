# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20170624_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approval',
            name='HR_rejects',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='approval',
            name='HR_selects_holds',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='approval',
            name='MR_rejects',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='approval',
            name='MR_selects_holds',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='approval',
            name='No_offers_processed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='approval',
            name='No_offers_released',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='approval',
            name='TR_rejects',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='approval',
            name='TR_selects_holds',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='approval',
            name='no_cv_shared',
            field=models.IntegerField(default=0),
        ),
    ]