from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from todo.validators import validate_indian_phone_number


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

    def __str__(self):
        return f"{self.title}- # {self.id}"


class Review(TimeStampModel):
    reviewer = models.CharField(max_length=100)
    review_title = models.CharField(max_length=85)

    task = models.ForeignKey(to=Task, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reviewer} - {self.review_title} - # {self.id}"


class Profile(TimeStampModel):
    user = models.OneToOneField(to=User, on_delete=models.PROTECT)
    phone = PhoneNumberField(validators=[validate_indian_phone_number])

    def __str__(self):
        return self.user.username
