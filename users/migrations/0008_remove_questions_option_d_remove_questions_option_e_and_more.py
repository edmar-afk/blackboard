# Generated by Django 5.0.4 on 2024-05-06 12:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_lesson_upload_date_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='option_D',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='option_E',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='takers',
        ),
        migrations.AddField(
            model_name='quizz',
            name='takers',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 6, 12, 9, 16, 413414, tzinfo=datetime.timezone.utc)),
        ),
    ]
