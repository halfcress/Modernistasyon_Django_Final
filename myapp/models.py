from django.db import models

class Sirket(models.Model):
    isim = models.CharField(max_length=20)
    resim = models.FileField(default="static/images/sirket-gorsel-e1643089635413_Nygl2Qy.jpg")
    def __str__(self):
        return f"{self.isim}"

class Proje(models.Model):
    ad = models.CharField(max_length=20)
    total = models.DecimalField(max_digits=20,decimal_places=0)
    miktar = models.DecimalField(max_digits=20,decimal_places=0)
    tarih = models.DateField()
    firma = models.ForeignKey(Sirket, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.ad}"

class Arac(models.Model):
    tip = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.tip}"

class Santiye(models.Model):
    isim = models.CharField(max_length=20)
    miktar = models.DecimalField(max_digits=20, decimal_places=0, default=0)
    araclar = models.ManyToManyField(Arac)
    baglanti = models.ForeignKey(Proje, on_delete=models.CASCADE)
    resim = models.FileField(default="static/images/636407734632442_h8daafR.jpg")
    def __str__(self):
        return f"{self.isim}"
    
class Personel(models.Model):
    ad = models.CharField(max_length=50)
    cinsiyet = models.CharField(max_length=10)
    yas = models.DecimalField(max_digits=4, decimal_places=0)
    baslamaTarih = models.DateField()
    resim = models.FileField(default="static/images/avatar.jpg")
    birim = models.ForeignKey(Santiye, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.ad}"        
    
class Tarih(models.Model):
    odenen_proje = models.CharField(max_length=30, null=True)
    odenen_santiye = models.CharField(max_length=30, null=True)
    odenen_tutar = models.DecimalField(max_digits=20, decimal_places=0, null=True)
    tarih = models.CharField(max_length=13, null=True)
    aciklama = models.CharField(max_length=100, null=True)
    def __str__(self):
        return f"{self.tarih}"

class Aciklama(models.Model):
    aciklama = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.aciklama}"