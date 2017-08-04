# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import openedx.core.djangoapps.xmodule_django.models


class Migration(migrations.Migration):

    dependencies = [
        ('course_overviews', '0013_courseoverview_language'),
        ('student', '0010_auto_20170207_0458'),
    ]

    operations = [
        # Pin the db_columns to the names already in the database
        migrations.AlterField(
            model_name='courseenrollment',
            name='course_id',
            field=openedx.core.djangoapps.xmodule_django.models.CourseKeyField(max_length=255, db_index=True, db_column='course_id'),
        ),
        migrations.AlterField(
            model_name='historicalcourseenrollment',
            name='course_id',
            field=openedx.core.djangoapps.xmodule_django.models.CourseKeyField(max_length=255, db_index=True, db_column='course_id'),
        ),

        # Rename the fields in Django to the new names that we want them to have
        migrations.RenameField(
            model_name='courseenrollment',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='historicalcourseenrollment',
            old_name='course_id',
            new_name='course',
        ),

        # Alter the fields to make them ForeignKeys (leaving off the db_constraint so
        # that we don't create it at migration time). The db_column is left off because
        # it defaults to ${field_name}_id, which we pinned it to up above.
        migrations.AlterField(
            model_name='courseenrollment',
            name='course',
            field=models.ForeignKey(db_constraint=False, to='course_overviews.CourseOverview'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historicalcourseenrollment',
            name='course',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='course_overviews.CourseOverview', null=True),
            preserve_default=True,
        ),

        # Set the Django-side unique-together and ordering configuration (no SQL required)
        migrations.AlterModelOptions(
            name='courseenrollment',
            options={'ordering': ('user', 'course')},
        ),
        migrations.AlterUniqueTogether(
            name='courseenrollment',
            unique_together=set([('user', 'course')]),
        ),
    ]
