from django.db import models
from django.db.models import CASCADE

from apps.visitors.models import Event


class Click(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=CASCADE)
