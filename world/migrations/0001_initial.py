# Generated by Django 4.2.6 on 2023-11-11 01:47

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Note",
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
                (
                    "note_heading",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("note", models.CharField(blank=True, max_length=1000, null=True)),
                ("lat", models.FloatField()),
                ("lng", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="WorldBorder",
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
                ("name", models.CharField(max_length=50)),
                ("area", models.IntegerField()),
                ("pop2005", models.IntegerField(verbose_name="Population 2005")),
                (
                    "fips",
                    models.CharField(max_length=2, null=True, verbose_name="FIPS Code"),
                ),
                ("iso2", models.CharField(max_length=2, verbose_name="2 Digit ISO")),
                ("iso3", models.CharField(max_length=3, verbose_name="3 Digit ISO")),
                ("un", models.IntegerField(verbose_name="United Nations Code")),
                ("region", models.IntegerField(verbose_name="Region Code")),
                ("subregion", models.IntegerField(verbose_name="Sub-Region Code")),
                ("lon", models.FloatField()),
                ("lat", models.FloatField()),
                (
                    "mpoly",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                (
                    "location",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, default=None, editable=False, null=True, srid=4326
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
