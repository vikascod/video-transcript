from django.db import models


class Video(models.Model):
    video_url = models.URLField()
    transcript = models.TextField(blank=True)
    


