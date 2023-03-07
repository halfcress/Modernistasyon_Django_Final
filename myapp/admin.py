from django.contrib import admin
from .models import Personel, Sirket, Proje, Arac, Santiye,Tarih, Aciklama



admin.site.register(Arac)
admin.site.register(Proje)
admin.site.register(Sirket)
admin.site.register(Santiye)
admin.site.register(Personel)
admin.site.register(Tarih)
admin.site.register(Aciklama)