from django.db import models
from django.utils import timezone
from users.models import User

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(User, null = False, on_delete=models.CASCADE, related_name="projects")
    pub_date = models.DateTimeField('date published', auto_now_add = True)

    def __str__(self):
        return self.title
