from django.db import models


class Job(models.Model):
    """Custom model for jobs
    Attributes:
        image (image): images for jobs
        summary (text): summaries for jobs
    """
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        """way jobs are represented in admin"""
        return self.summary
