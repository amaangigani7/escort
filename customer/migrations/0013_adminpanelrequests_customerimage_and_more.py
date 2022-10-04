# Generated by Django 4.1.1 on 2022-10-04 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "customer",
            "0012_customer_about_customer_hair_color_customer_height_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="AdminPanelRequests",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sent_at", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "req_type",
                    models.CharField(
                        choices=[
                            ("Publish", "Publish"),
                            ("Verification", "Verification"),
                        ],
                        default="Publish",
                        max_length=255,
                    ),
                ),
                ("verify", models.BooleanField(default=False)),
                ("publish", models.BooleanField(default=False)),
                ("img_1", models.TextField(blank=True, null=True)),
                ("img_2", models.TextField(blank=True, null=True)),
                ("img_3", models.TextField(blank=True, null=True)),
                ("img_4", models.TextField(blank=True, null=True)),
                (
                    "customer",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomerImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("img_1", models.TextField(blank=True, null=True)),
                ("img_2", models.TextField(blank=True, null=True)),
                ("img_3", models.TextField(blank=True, null=True)),
                ("img_4", models.TextField(blank=True, null=True)),
                (
                    "customer",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="CustomerImages",),
    ]
