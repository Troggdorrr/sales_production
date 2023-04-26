# Generated by Django 4.1.3 on 2023-04-25 08:31

from django.conf import settings
from django.contrib.postgres.operations import TrigramExtension
import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import products.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        TrigramExtension(),
        migrations.CreateModel(
            name="City",
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
                    "name",
                    models.CharField(
                        max_length=60, unique=True, verbose_name="Название города"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Donor",
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
                    "name",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="Название сайта"
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        upload_to=products.models.get_logo_upload_to,
                        verbose_name="Логотип сайта",
                    ),
                ),
                ("url", models.URLField(verbose_name="URL сайта")),
            ],
        ),
        migrations.CreateModel(
            name="PromoType",
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
                    "name",
                    models.CharField(
                        max_length=30, unique=True, verbose_name="Название"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Shop",
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
                    "address",
                    models.CharField(max_length=100, verbose_name="Адрес магазина"),
                ),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shops",
                        to="products.city",
                        verbose_name="Город",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Promo",
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
                ("date_begin", models.DateField(verbose_name="Дата начала")),
                ("date_end", models.DateField(verbose_name="Дата окончания")),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="promo",
                        to="products.promotype",
                        verbose_name="Тип акции",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                    "title",
                    models.CharField(max_length=255, verbose_name="Название товара"),
                ),
                (
                    "poster",
                    models.URLField(blank=True, null=True, verbose_name="Постер"),
                ),
                ("price", models.FloatField(verbose_name="Цена")),
                ("promo_price", models.FloatField(verbose_name="Цена по скидке")),
                ("url", models.URLField(verbose_name="Ссылка на товар")),
                (
                    "search_vector",
                    django.contrib.postgres.search.SearchVectorField(null=True),
                ),
                (
                    "donor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="shops",
                        to="products.donor",
                        verbose_name="Сайт",
                    ),
                ),
                (
                    "promo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="products.promo",
                        verbose_name="Акция",
                    ),
                ),
                (
                    "shops",
                    models.ManyToManyField(
                        to="products.shop", verbose_name="В магазинах"
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.CreateModel(
            name="Like",
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
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to="products.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="product",
            index=django.contrib.postgres.indexes.GistIndex(
                fields=["title"], name="gist_index", opclasses=["gist_trgm_ops"]
            ),
        ),
        migrations.AddIndex(
            model_name="product",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_vector"], name="products_pr_search__98d711_gin"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="like",
            unique_together={("product", "user")},
        ),
    ]
