# Generated by Django 4.2.7 on 2023-11-15 05:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="city2",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
    ]
