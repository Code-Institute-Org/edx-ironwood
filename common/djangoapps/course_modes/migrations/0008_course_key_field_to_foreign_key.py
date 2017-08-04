# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import openedx.core.djangoapps.xmodule_django.models


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0013_courseoverview_language'),
        ('course_modes', '0007_coursemode_bulk_sku'),
    ]

    operations = [
        # Pin the name of the column in the database so that we can rename the field
        # in Django without generating any sql changes
        migrations.AlterField(
            model_name='coursemode',
            name='course_id',
            field=openedx.core.djangoapps.xmodule_django.models.CourseKeyField(max_length=255, db_index=True, verbose_name="Course", db_column='course_id'),
        ),
        # Change the field name in Django to match our target field name
        migrations.RenameField(
            model_name='coursemode',
            old_name='course_id',
            new_name='course',
        ),
        # Change the type of the field in Django to be a foreign key
        # N.B. we don't need the db_column declaration because the default
        # for Django is to use ${field_name}_id (which is what we pinned the column
        # name to above).
        # We deliberately leave db_constraint set to False because the column
        # isn't currently constrained
        migrations.AlterField(
            model_name='coursemode',
            name='course',
            field=models.ForeignKey(related_name='modes', db_constraint=False, default=None, to='course_overviews.CourseOverview'),
            preserve_default=False,
        ),
        # Change the Django unique-together constraint (this is Django-level only
        # since the database column constraint already exists).
        migrations.AlterUniqueTogether(
            name='coursemode',
            unique_together=set([('course', 'mode_slug', 'currency')]),
        ),
    ]
