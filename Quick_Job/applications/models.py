from django.db import models
from django.conf import settings
from jobs.models import Job

# Create your models here.

User = settings.AUTH_USER_MODEL

class Application(models.Model):
    STATUS_PENDING = "PENDING"
    STATUS_ACCEPTED = "ACCEPTED"
    STATUS_REJECTED = "REJECTED"
    STATUS_SUBMITTED = "SUBMITTED"
    STATUS_SHORTLISTED = "SHORTLISTED"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_REJECTED, "Rejected"),
        (STATUS_SUBMITTED, "Submitted"),
        (STATUS_SHORTLISTED, "Shortlisted"),
    ]

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    cover_letter = models.TextField()


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='SUBMITTED'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("job", "applicant")

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"