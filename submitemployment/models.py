import uuid, os

from django.db import models
from django.conf import settings

def cv_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("uploads/cv_files/", filename)

# Create your models here.
class SubmitEmployment(models.Model):
    """SubmitEmployment model"""

    motivation_on_employment = models.TextField()
    submiter = models.ForeignKey(
        'client.Client',
        on_delete=models.CASCADE,
    )
    employment = models.ForeignKey(
        'employments.Employments',
        on_delete=models.CASCADE,
    )

    cv_file = models.FileField(null=True, upload_to=cv_file_path, blank=True)

    def __str__(self):
        return self.email