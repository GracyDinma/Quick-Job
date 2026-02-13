from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Application
from .serializers import ApplicationSerializer
from users.permissions import IsAdmin, IsApplicant

# Create your views here.
class ApplicationListCreateView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        
        # Admin sees all
        if user.role == "ADMIN":
            return Application.objects.select_related("job", "applicant")
        
        # Applicant sees only their applications
        return Application.objects.filter(
            applicant=user
        ).select_related("job")
    
    def perform_create(self, serializer):
        user = self.request.user

        # Only applicant can create applications
        if user.role != "APPLICANT":
            raise PermissionError("Only applicants can apply.")
        
        serializer.save(applicant=user)


class ApplicationDeleteView(generics.DestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
