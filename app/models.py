from django.db import models

# Create your models here.

class Library(models.Model):
    Book= models.CharField(max_length=100, primary_key=True)
    Author= models.CharField(max_length=100)
    Gmail= models.EmailField()
    Date= models.DateField()

    def __str__(self):
        return self.Author