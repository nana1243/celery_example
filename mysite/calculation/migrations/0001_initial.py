# Generated by Django 3.2.2 on 2021-05-08 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Balances",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("identify", models.CharField(max_length=20)),
                (
                    "amount",
                    models.DecimalField(decimal_places=4, max_digits=14),
                ),  # noqa: E501
            ],
        ),
        migrations.CreateModel(
            name="GetData",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("identify", models.CharField(max_length=20)),
                ("is_disabled", models.BooleanField(default=False)),
                (
                    "amount",
                    models.DecimalField(decimal_places=4, max_digits=14),
                ),  # noqa: E501
                ("last_payment", models.DateTimeField(blank=True, null=True)),
                ("next_payment", models.DateTimeField(blank=True, null=True)),
                ("timestamp", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="TransferAmount",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("identify", models.CharField(max_length=20)),
                (
                    "amount",
                    models.DecimalField(decimal_places=4, max_digits=14),
                ),  # noqa: E501
                ("timestamp", models.DateTimeField()),
            ],
        ),
    ]