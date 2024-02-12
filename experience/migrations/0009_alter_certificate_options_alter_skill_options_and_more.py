# Generated by Django 5.0.1 on 2024-02-12 06:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experience", "0008_alter_education_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="certificate",
            options={"ordering": ["display_order"]},
        ),
        migrations.AlterModelOptions(
            name="skill",
            options={"ordering": ["display_order"]},
        ),
        migrations.AlterModelOptions(
            name="technology",
            options={"ordering": ["display_order"]},
        ),
        migrations.AddField(
            model_name="certificate",
            name="display_order",
            field=models.PositiveIntegerField(
                default=0, help_text="Determines display order in the list"
            ),
        ),
        migrations.AddField(
            model_name="skill",
            name="display_order",
            field=models.PositiveIntegerField(
                default=0, help_text="Determines display order in the list"
            ),
        ),
        migrations.AddField(
            model_name="technology",
            name="display_order",
            field=models.PositiveIntegerField(
                default=0, help_text="Determines display order in the list"
            ),
        ),
    ]