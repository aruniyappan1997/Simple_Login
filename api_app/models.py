from django.db import models

# Create your models here.
class User_Details(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}@ksk.com"