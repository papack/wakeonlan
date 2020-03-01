from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.SlugField(unique=True)
    mac = models.CharField(max_length=12)
    desc = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name+"("+self.mac+")"
