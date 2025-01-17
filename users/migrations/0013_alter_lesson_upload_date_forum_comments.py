# Generated by Django 5.0.4 on 2024-05-06 13:53

import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_lesson_upload_date_alter_questions_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 6, 13, 53, 33, 166954, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('file', models.FileField(blank=True, null=True, upload_to='media/announcement', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'pdf', 'word', 'ppt', 'xlsx', 'csv', 'gif'])])),
                ('upload_date', models.DateTimeField(default=datetime.datetime(2024, 5, 6, 13, 53, 33, 166954, tzinfo=datetime.timezone.utc))),
                ('description', models.TextField()),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('comment_date', models.DateTimeField(default=datetime.datetime(2024, 5, 6, 13, 53, 33, 166954, tzinfo=datetime.timezone.utc))),
                ('commentors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.forum')),
            ],
        ),
    ]
