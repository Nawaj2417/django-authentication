# Generated by Django 5.1 on 2024-08-19 04:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="passwordresetrequest",
            name="token",
            field=models.CharField(
                default="mnkOlBRwxIRnCIqcIKH3vPnqQ9bxyCo4",
                editable=False,
                max_length=32,
                unique=True,
            ),
        ),
    ]
