# from django.urls import path,include
# from .views import UserViewSet, ProfileViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'profiles', ProfileViewSet)

# urlpatterns = [
#     path('', include(router.urls)),


# ]


# accounts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
