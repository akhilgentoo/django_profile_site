# Generated by Django 5.0.4 on 2024-06-18 13:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mydetails", "0014_rename_education_category_education_category1"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Education_category_details",
            new_name="Education_category_details1",
        ),
    ]