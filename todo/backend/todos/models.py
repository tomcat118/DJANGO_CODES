# define our models here to include title and body info only, which is our task and details about each task
from django.db import models


# Create your models here.
class Todo (models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title