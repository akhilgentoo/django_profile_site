# Generated by Django 5.0.4 on 2024-06-20 04:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mydetails", "0018_alter_experience1_exp1_year_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aboutpage",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp1_desc",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp2_desc",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp3_desc",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp4_desc",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp5_desc",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp6_desc",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp7_desc",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="experience1",
            name="exp7_year",
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name="skills1",
            name="skill1_description",
            field=models.TextField(),
        ),
    ]