# Generated by Django 5.0.1 on 2024-02-14 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="year",
        ),
        migrations.AddField(
            model_name="project",
            name="date",
            field=models.DateField(),
        ),
    ]
