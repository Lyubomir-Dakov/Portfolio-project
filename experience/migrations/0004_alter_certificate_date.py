# Generated by Django 5.0.1 on 2024-02-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experience", "0003_certificate_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificate",
            name="date",
            field=models.CharField(),
        ),
    ]