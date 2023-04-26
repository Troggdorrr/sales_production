from rest_framework.routers import SimpleRouter

from rest_framework_nested.routers import NestedSimpleRouter

from .views import UserViewSet, UserLikesViewSet


router = SimpleRouter()
router.register("users", UserViewSet, "users")

user_router = NestedSimpleRouter(router, "users", lookup="user")
user_router.register("likes", UserLikesViewSet, "user_likes")

urlpatterns = router.urls + user_router.urls
