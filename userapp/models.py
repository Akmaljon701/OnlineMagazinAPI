from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    jins = models.CharField(max_length=7)
    shahar = models.CharField(max_length=50, blank=True)
    tugilgan_sana = models.DateField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism
