from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
METHODS = (
    ('C', 'Cleaning'),
    ('R', 'Restoration'),
    ('M', 'Maintenance')
)

class Art(models.Model):
    name = models.CharField(max_length=100)
    painting_by = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    medium = models.CharField(max_length=100)

    def fed_for_today(self):
        return self.maintaining_set.filter(date=date.today()).count() >= len(METHODS)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'art_id': self.id})

class Maintaining(models.Model):
  date = models.DateField('Maintenance Date')
  method = models.CharField(max_length=1, choices=METHODS,default=METHODS[0][0])
  
  art = models.ForeignKey(Art, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_method_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']