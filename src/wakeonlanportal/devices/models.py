from django.db import models
from macaddress.fields import MACAddressField

# Create your models here.

class Device(models.Model):
    name = models.SlugField(unique=True)
    mac = MACAddressField(null=False, blank=False)
    desc = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name+"("+str(self.mac)+")"
