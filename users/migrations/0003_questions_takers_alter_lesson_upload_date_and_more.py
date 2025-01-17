# Generated by Django 5.0.4 on 2024-05-06 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_questions_type_alter_quizz_deadline_lesson'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='takers',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 6, 5, 25, 18, 515335, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='quizz',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 6, 5, 25, 18, 515335, tzinfo=datetime.timezone.utc)),
        ),
    ]
