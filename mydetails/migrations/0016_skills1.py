# Generated by Django 5.0.4 on 2024-06-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "mydetails",
            "0015_rename_education_category_details_education_category_details1",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="skills1",
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
                ("skill1_description", models.CharField(max_length=500)),
                ("sk1", models.CharField(max_length=500)),
                ("sk1_percentage", models.CharField(max_length=500)),
                ("sk2", models.CharField(max_length=500)),
                ("sk2_percentage", models.CharField(max_length=500)),
                ("sk3", models.CharField(max_length=500)),
                ("sk3_percentage", models.CharField(max_length=500)),
                ("sk4", models.CharField(max_length=500)),
                ("sk4_percentage", models.CharField(max_length=500)),
                ("sk5", models.CharField(max_length=500)),
                ("sk5_percentage", models.CharField(max_length=500)),
                ("sk6", models.CharField(max_length=500)),
                ("sk6_percentage", models.CharField(max_length=500)),
                ("sk7", models.CharField(max_length=500)),
                ("sk7_percentage", models.CharField(max_length=500)),
                ("sk8", models.CharField(max_length=500)),
                ("sk8_percentage", models.CharField(max_length=500)),
                ("sk9", models.CharField(max_length=500)),
                ("sk9_percentage", models.CharField(max_length=500)),
                ("sk10", models.CharField(max_length=500)),
                ("sk10_percentage", models.CharField(max_length=500)),
            ],
        ),
    ]