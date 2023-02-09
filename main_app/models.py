from django.db import models

# Create your models here.
class Art(models.Model):
    name = models.CharField(max_length=100)
    painting_by = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    medium = models.CharField(max_length=100)

    def __str__(self):
        return self.name