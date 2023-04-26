from django.contrib import admin

from products.models import Shop, Donor, City, Product, Promo, PromoType, Like


admin.site.register([Shop, Donor, City, Product, Promo, PromoType, Like])