from __future__ import unicode_literals

from django.db import models

class Polygon(models.Model):
    encoded = models.TextField()
    post_date = models.DateTimeField()