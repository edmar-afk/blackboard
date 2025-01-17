# Generated by Django 5.0.4 on 2024-05-07 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_comments_comment_date_alter_forum_upload_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizz',
            name='takers',
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 10, 47, 18, 223437, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 10, 47, 18, 223437, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 10, 47, 18, 223437, tzinfo=datetime.timezone.utc)),
        ),
    ]
