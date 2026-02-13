from django.shortcuts import render
from rest_framework import generics, permissions, filters
from .models import Job
from .serializers import JobSerializer
from users.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all().select_related()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['location', 'job_type']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsAdmin()]
        return [IsAuthenticated()]
        
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)