from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.


class Film(models.Model):
    title=models.CharField(max_length=100,blank=False)
    length=models.PositiveIntegerField(blank=True,null=True)
    year=models.PositiveIntegerField(blank=True,null=True)
    score=models.FloatField(blank=True,null=True,validators=[MinValueValidator(0),MaxValueValidator(10)])

    def __str__(self):
        if self.year:
            return f" {self.title} ({self.year}) "
        return self.title    

