from django.db import models
from userapp.models import Profil

class Bolim(models.Model):
    nom = models.CharField(max_length=30)
    rasm = models.FileField(null=True, blank=True, upload_to='bolimlar')

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    batafsil = models.TextField(blank=True)
    narx = models.PositiveIntegerField()
    chegrma = models.PositiveIntegerField(default=0)
    rasm = models.FileField(null=True, blank=True, upload_to='mahsulotlar')
    mavjud = models.BooleanField(default=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Izoh(models.Model):
    matn = models.CharField(max_length=300)
    reyting = models.PositiveSmallIntegerField()
    sana = models.DateField(auto_now_add=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)

    def __str__(self):
        return self.matn