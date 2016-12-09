# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoringCore', '0002_auto_20161124_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Textbook_Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.IntegerField()),
                ('chapterName', models.CharField(max_length=45)),
                ('section', models.IntegerField()),
                ('sectionName', models.CharField(max_length=45)),
                ('topicCount', models.IntegerField()),
                ('textbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoringCore.Textbook')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='card',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='teacher_classes',
            unique_together=set([('teacher', 'school', 'grade', 'classes', 'textbook')]),
        ),
        migrations.AlterUniqueTogether(
            name='textbook_section',
            unique_together=set([('textbook', 'chapter', 'section')]),
        ),
    ]