from django.urls import path, include
from .views import ProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("add-product/",ProductView)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',include(router.urls)),
]