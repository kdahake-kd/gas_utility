# from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth import get_user_model
# from .models import ServiceRequest, ServiceRequestStatus
# from .serializers import ServiceRequestSerializer, ServiceRequestStatusSerializer

# User = get_user_model()

# class ServiceRequestViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = ServiceRequest.objects.all()
#     serializer_class = ServiceRequestSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class ServiceRequestStatusViewSet(viewsets.ModelViewSet):
#     queryset = ServiceRequestStatus.objects.all()
#     serializer_class = ServiceRequestStatusSerializer


# service_requests/views.py
from rest_framework import viewsets
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return ServiceRequest.objects.all()
        return ServiceRequest.objects.filter(user=self.request.user)


