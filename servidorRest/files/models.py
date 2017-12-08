from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings

UPLOADS_DIR = getattr(settings, "UPLOADS_DIR", "uploads")

class FILE(models.Model):
    file = models.FileField(upload_to = UPLOADS_DIR)
    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now_add = True, auto_now = True)
