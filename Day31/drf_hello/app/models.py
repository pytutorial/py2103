from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    createdDate = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# python manage.py makemigrations
# python manage.py migrate
