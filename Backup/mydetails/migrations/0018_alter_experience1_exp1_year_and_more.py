# Generated by Django 5.0.4 on 2024-06-20 04:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mydetails", "0017_experience1"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience1",
            name="exp1_year",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp2_year",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp3_year",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp4_year",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp5_year",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp6_year",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp7_year",
            field=models.IntegerField(),
        ),
    ]