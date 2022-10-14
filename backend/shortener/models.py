from django.db import models
from rest_framework.reverse import reverse


class ShortenedUrl(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    long_url = models.URLField()
    code = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "shortened_urls"
