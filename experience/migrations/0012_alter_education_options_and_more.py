# Generated by Django 5.0.1 on 2024-02-14 05:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("experience", "0011_education_display_order_work_display_order"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="education",
            options={"ordering": ["-start_date"]},
        ),
        migrations.RemoveField(
            model_name="education",
            name="display_order",
        ),
        migrations.RemoveField(
            model_name="work",
            name="display_order",
        ),
    ]