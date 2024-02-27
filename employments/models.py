from django.db import models
import uuid,os

def recipe_image_file_path(instance, filename):
    """Generate file path for new empl image"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"

    return os.path.join("uploads/products/", filename)


class Employments(models.Model):
    """Employments model"""
    created_at = models.DateField(auto_now=True)
    name = models.CharField(max_length=255, )
    description = models.TextField()

    creator = models.ForeignKey(
        'enterprise.Enterprise',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
