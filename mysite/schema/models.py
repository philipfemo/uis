from django.db import models
from users.models import User as user

# Create your models here.

DAYS = (
    ("mon", "Monday"),
    ("thu", "Thursday"),
)

class SlotField(models.Model):
    start_time = models.TimeField()
    day = models.CharField(choices=DAYS, max_length=3)

class Choice(models.Model):
    slot = models.ForeignKey(SlotField, on_delete=models.CASCADE, unique=True, related_name="choices")
    owner = models.ForeignKey(user, on_delete=models.CASCADE, related_name="choices")
