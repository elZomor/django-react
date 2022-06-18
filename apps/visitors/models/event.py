from django.db import models


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    facebook_link = models.CharField(max_length=300)
    image = models.FileField(upload_to="images/", null=True, blank=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
