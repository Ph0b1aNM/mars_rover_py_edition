from django.db import models

# Mars Rover Input Table

class MRInputs(models.Model):
    sopx = models.IntegerField(default=0)
    sopy = models.IntegerField(default=0)
    r1px = models.IntegerField(default=0)
    r1py = models.IntegerField(default=0)
    r1pface = models.CharField(max_length=50)
    inst1 = models.CharField(max_length=50)
    r2px = models.IntegerField(default=0)
    r2py = models.IntegerField(default=0)
    r2pface = models.CharField(max_length=50)
    inst2 = models.CharField(max_length=50)