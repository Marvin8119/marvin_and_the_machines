from django.db import models

# Create your models here.
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
