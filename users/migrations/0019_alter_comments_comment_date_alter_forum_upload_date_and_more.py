# Generated by Django 5.0.4 on 2024-05-07 13:55

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_remove_quizz_takers_alter_comments_comment_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 13, 55, 50, 240997, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 13, 55, 50, 240997, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 13, 55, 50, 240997, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2024, 5, 7, 13, 55, 50, 240997, tzinfo=datetime.timezone.utc))),
                ('description', models.TextField()),
                ('like', models.IntegerField()),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
