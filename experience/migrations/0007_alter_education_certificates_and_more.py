# Generated by Django 5.0.1 on 2024-02-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experience", "0006_rename_specialty_education_speciality"),
    ]

    operations = [
        migrations.AlterField(
            model_name="education",
            name="certificates",
            field=models.ManyToManyField(
                blank=True, to="experience.certificate", verbose_name="Certificates"
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="end_date",
            field=models.DateField(blank=True, null=True, verbose_name="Graduate"),
        ),
        migrations.AlterField(
            model_name="education",
            name="location",
            field=models.CharField(max_length=100, verbose_name="Location"),
        ),
        migrations.AlterField(
            model_name="education",
            name="logo_svg",
            field=models.TextField(
                blank=True, help_text="Paste your SVG code here.", verbose_name="Logo"
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="name",
            field=models.CharField(
                max_length=50, verbose_name="School or University name"
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="skills",
            field=models.ManyToManyField(
                blank=True, to="experience.skill", verbose_name="Skills"
            ),
        ),
        migrations.AlterField(
            model_name="education",
            name="speciality",
            field=models.CharField(max_length=100, verbose_name="Speciality"),
        ),
        migrations.AlterField(
            model_name="education",
            name="start_date",
            field=models.DateField(verbose_name="Start school or university"),
        ),
        migrations.AlterField(
            model_name="education",
            name="technologies",
            field=models.ManyToManyField(
                blank=True, to="experience.technology", verbose_name="Technologies"
            ),
        ),
        migrations.AlterField(
            model_name="work",
            name="end_date",
            field=models.DateField(blank=True, null=True, verbose_name="Leave work"),
        ),
        migrations.AlterField(
            model_name="work",
            name="location",
            field=models.CharField(max_length=100, verbose_name="Location"),
        ),
        migrations.AlterField(
            model_name="work",
            name="logo_svg",
            field=models.TextField(
                blank=True, help_text="Paste your SVG code here.", verbose_name="Logo"
            ),
        ),
        migrations.AlterField(
            model_name="work",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Company name"),
        ),
        migrations.AlterField(
            model_name="work",
            name="skills",
            field=models.ManyToManyField(
                blank=True, to="experience.skill", verbose_name="Skills"
            ),
        ),
        migrations.AlterField(
            model_name="work",
            name="start_date",
            field=models.DateField(verbose_name="Start work"),
        ),
        migrations.AlterField(
            model_name="work",
            name="technologies",
            field=models.ManyToManyField(
                blank=True, to="experience.technology", verbose_name="Technologies"
            ),
        ),
        migrations.AlterField(
            model_name="work",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Working position"),
        ),
    ]
