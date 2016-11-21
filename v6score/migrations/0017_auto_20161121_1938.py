# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-21 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v6score', '0016_auto_20161120_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='finished',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='manual',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='nat64_image_score',
            field=models.FloatField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='nat64_resource_score',
            field=models.FloatField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='requested',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='started',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='url',
            field=models.URLField(db_index=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='v6only_image_score',
            field=models.FloatField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='v6only_resource_score',
            field=models.FloatField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterIndexTogether(
            name='measurement',
            index_together=set([('v6only_resource_score', 'nat64_resource_score'), ('v6only_image_score', 'nat64_image_score')]),
        ),
    ]
