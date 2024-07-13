# Generated by Django 5.0.4 on 2024-06-18 12:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mydetails", "0011_rename_hobbies_hobbies1"),
    ]

    operations = [
        migrations.CreateModel(
            name="Eduction_category",
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
                ("ed1", models.CharField(max_length=500)),
                ("ed2", models.CharField(max_length=500)),
                ("ed3", models.CharField(max_length=500)),
                ("ed4", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="Eduction_category_details",
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
                ("ed1_details", models.CharField(max_length=500)),
                ("ed2_details", models.CharField(max_length=500)),
                ("ed3_details", models.CharField(max_length=500)),
                ("ed4_details", models.CharField(max_length=500)),
            ],
        ),
    ]