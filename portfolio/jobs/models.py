from django.db import models


class Job(models.Model):
    """Custom model for jobs
    Attributes:
        images (image): images for jobs
        summary (text): summaries for jobs
    """
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
