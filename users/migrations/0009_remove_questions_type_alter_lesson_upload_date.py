# Generated by Django 5.0.4 on 2024-05-06 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_questions_option_d_remove_questions_option_e_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='type',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 6, 12, 16, 1, 522145, tzinfo=datetime.timezone.utc)),
        ),
    ]
