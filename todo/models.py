from django.db import models


# Create your models here.

class TimeStampModel(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(TimeStampModel):
    title = models.CharField(max_length=85)
    content = models.CharField(max_length=300)
    date_posted = models.DateTimeField(auto_now_add=True)


