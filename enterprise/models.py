from django.db import models
from django.conf import settings

# Create your models here.
class Enterprise(models.Model):
    """Enterprise model"""

    name = models.CharField(max_length=255, )
    description = models.CharField(max_length=255,default="" )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name