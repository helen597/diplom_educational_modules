# Generated by Django 5.0.6 on 2024-06-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("modules", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="module",
            name="description",
            field=models.TextField(
                blank=True,
                null=True,
                verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="module",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Название"),
        ),
    ]
