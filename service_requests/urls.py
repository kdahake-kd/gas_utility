
# from django.urls import path,include
# from .views import ServiceRequestViewSet, ServiceRequestStatusViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'service_requests', ServiceRequestViewSet)
# router.register(r'service_request_statuses', ServiceRequestStatusViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
   
# ]



# service_requests/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet

router = DefaultRouter()
router.register(r'service_requests', ServiceRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
