# Generated by Django 3.1.1 on 2020-10-18 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("response", "0016_actions_auto_created_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="incident",
            name="mitigated",
            field=models.BooleanField(default=False),
        ),
    ]
