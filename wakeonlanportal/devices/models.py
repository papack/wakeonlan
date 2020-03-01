from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.SlugField()
    mac = models.CharField(max_length=10)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.name+"("+self.mac+")"
