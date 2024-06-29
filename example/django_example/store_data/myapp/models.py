from django.db import models

# Create your models here.
class Application(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    date_available = models.DateField()
    occupation = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"