from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    comment = models.TextField()


