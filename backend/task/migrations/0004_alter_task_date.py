# Generated by Django 4.1.5 on 2023-02-14 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task", "0003_alter_task_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
