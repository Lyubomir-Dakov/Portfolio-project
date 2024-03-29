# Generated by Django 5.0.1 on 2024-02-13 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experience", "0010_education_slug_work_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="education",
            name="display_order",
            field=models.PositiveIntegerField(
                default=0, help_text="Determines display order in the list"
            ),
        ),
        migrations.AddField(
            model_name="work",
            name="display_order",
            field=models.PositiveIntegerField(
                default=0, help_text="Determines display order in the list"
            ),
        ),
    ]
