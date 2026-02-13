from django.urls import path
from .views import ApplicationListCreateView, ApplicationDeleteView


urlpatterns = [
    path("", ApplicationListCreateView.as_view(), name="applications"),
    path("<int:pk>/delete/", ApplicationDeleteView.as_view(), name="application-delete"),
]