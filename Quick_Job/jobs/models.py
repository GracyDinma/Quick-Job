from django.db import models
from django.conf import settings


class Job(models.Model):
    FULL_TIME = "FULL_TIME"
    PART_TIME = "PART_TIME"
    CONTRACT = "CONTRACT"


    JOB_TYPE_CHOICES = [
        ('FULL_TIME', 'Full Time'),
        ('PART_TIME', 'Part Time'),
        ('CONTRACT', 'Contract'),
    ]

    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    industry = models.CharField(max_length=255, db_index=True)
    location = models.CharField(max_length=255, db_index=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title
