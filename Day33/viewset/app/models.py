from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    birthDate = models.DateTimeField()
    height = models.FloatField()
    weight = models.FloatField()
    goals = models.IntegerField()
    matches = models.IntegerField()

# python manage.py makemigrations --> generate db script
# python manage.py migrate --> execute db script