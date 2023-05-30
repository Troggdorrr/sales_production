from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.postgres.indexes import GistIndex
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector

import pathlib


class City(models.Model):
    name = models.CharField("Название города", max_length=60, unique=True)

    def __str__(self) -> str:
        return self.name


def get_logo_upload_to(instance, filename: str) -> str:
    extension = pathlib.Path(filename).suffix
    return "products/static/products/logo/{0}{1}".format(instance.name, extension)


class Donor(models.Model):
    name = models.CharField("Название сайта", max_length=30, unique=True)
    logo = models.ImageField("Логотип сайта", upload_to=get_logo_upload_to)
    url = models.URLField("URL сайта")

    def __str__(self) -> str:
        return self.name


class Shop(models.Model):
    address = models.CharField("Адрес магазина", max_length=200)
    city = models.ForeignKey(
        City, verbose_name="Город", on_delete=models.CASCADE, related_name="shops"
    )

    def __str__(self) -> str:
        return self.address


class PromoType(models.Model):
    name = models.CharField("Название", max_length=30, unique=True)

    def __str__(self) -> str:
        return self.name


class Promo(models.Model):
    date_begin = models.DateField("Дата начала")
    date_end = models.DateField("Дата окончания")
    type = models.ForeignKey(
        PromoType,
        verbose_name="Тип акции",
        on_delete=models.CASCADE,
        related_name="promo",
    )


class Product(models.Model):
    title = models.CharField("Название товара", max_length=255)
    poster = models.CharField("Постер", null=True, blank=True, max_length=500)
    price = models.FloatField("Цена")
    promo_price = models.FloatField("Цена по скидке")
    url = models.URLField("Ссылка на товар")
    shops = models.ManyToManyField(Shop, verbose_name="В магазинах")
    promo = models.ForeignKey(
        Promo, verbose_name="Акция", on_delete=models.CASCADE, related_name="products"
    )
    donor = models.ForeignKey(
        Donor, verbose_name="Сайт", on_delete=models.CASCADE, related_name="shops"
    )
    search_vector = SearchVectorField(null=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        Product.objects.filter(pk=self.pk).update(search_vector=SearchVector("title"))

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        indexes = [
            GistIndex(name="gist_index", fields=["title"], opclasses=["gist_trgm_ops"]),
            GinIndex(fields=["search_vector"]),
        ]


class Like(models.Model):
    product = models.ForeignKey(Product, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(), related_name="likes", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ["product", "user"]
