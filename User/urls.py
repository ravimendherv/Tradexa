from django.urls import path, include
from .views import UserRegistrationView,PostView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('userRegistration',UserRegistrationView)
router.register('post',PostView)

urlpatterns = [
    path('',include(router.urls)),
]