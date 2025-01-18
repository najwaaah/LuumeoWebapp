# Generated by Django 5.1.5 on 2025-01-17 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="media/course")),
                ("description", models.TextField()),
                ("full_name", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Course",
                "verbose_name_plural": "course",
            },
        ),
    ]
