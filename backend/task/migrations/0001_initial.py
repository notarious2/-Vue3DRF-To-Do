# Generated by Django 4.1.5 on 2023-02-14 08:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "task_id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("priority", models.IntegerField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("text", models.TextField()),
                ("completed", models.BooleanField(default=False)),
            ],
        ),
    ]
