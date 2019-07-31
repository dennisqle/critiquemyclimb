from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Climb(models.Model):
    poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    grade = models.IntegerField()
    is_outdoor = models.BooleanField()
    description = models.TextField(max_length=200)
    video_url = models.URLField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


