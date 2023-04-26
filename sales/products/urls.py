from rest_framework.routers import SimpleRouter

from rest_framework_nested.routers import NestedSimpleRouter

from .views import (
    ProductViewSet,
    CityViewSet,
    DonorViewSet,
    PromoTypeViewSet,
    ShopViewSet,
    ProductLikesViewSet,
    SimiliarViewSet
)


router = SimpleRouter()
router.register("products", ProductViewSet, "products")
router.register("cities", CityViewSet, "cities")
router.register("donors", DonorViewSet, "donors")
router.register("promotypes", PromoTypeViewSet, "promotypes")

product_router = NestedSimpleRouter(router, "products", lookup="product")
product_router.register("shops", ShopViewSet, "product_shops")
product_router.register("likes", ProductLikesViewSet, "product_likes")
product_router.register("similiar", SimiliarViewSet, "product_similiar")

urlpatterns = router.urls + product_router.urls
