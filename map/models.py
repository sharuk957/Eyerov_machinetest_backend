from django.db import models

# Create your models here.

class Imagedata(models.Model):
    title = models.CharField(max_length=250)
    coords = models.CharField(max_length=250)
    shape = models.CharField(max_length=250)

    def __str__(self):
        return self.title