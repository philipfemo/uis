from django.db import models
from users.models import User as user

# Create your models here.
class SlotField(models.Model):
    owner = models.ForeignKey(user)
    status = models.BooleanField(default=True)

class MonSlots(models.Model):
    slot01 = models.ForeignKey(SlotField)
    slot02 = models.ForeignKey(SlotField)
    slot03 = models.ForeignKey(SlotField)
    slot04 = models.ForeignKey(SlotField)
    slot05 = models.ForeignKey(SlotField)
    slot06 = models.ForeignKey(SlotField)
    slot07 = models.ForeignKey(SlotField)
    slot08 = models.ForeignKey(SlotField)
    slot09 = models.ForeignKey(SlotField)
    slot10 = models.ForeignKey(SlotField)
    slot11 = models.ForeignKey(SlotField)
    slot12 = models.ForeignKey(SlotField)

class ThurSlots(models.Model):
    slot01 = models.ForeignKey(SlotField)
    slot02 = models.ForeignKey(SlotField)
    slot03 = models.ForeignKey(SlotField)
    slot04 = models.ForeignKey(SlotField)
    slot05 = models.ForeignKey(SlotField)
    slot06 = models.ForeignKey(SlotField)
    slot07 = models.ForeignKey(SlotField)
    slot08 = models.ForeignKey(SlotField)
    slot09 = models.ForeignKey(SlotField)
    slot10 = models.ForeignKey(SlotField)
    slot11 = models.ForeignKey(SlotField)
    slot12 = models.ForeignKey(SlotField)
