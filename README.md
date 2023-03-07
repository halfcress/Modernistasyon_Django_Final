# Modernistasyon_Final
 
**Anasayfa :** http://127.0.0.1:8000/anasayfa/

**Kullanıcı adı:** admin
**Şifre:** admin123

**ER-Diagram:**

![alt text](https://github.com/halfcress/Modernistasyon_Django_Final/blob/main/ER-diagram.png?raw=true)

**Random personel oluşturmak için kullandığım algoritma:**

```
ad = ['Ahmet', 'Mehmet', 'Cengiz', 'Deniz', 'Rafet', 'Ali', 'Mahmut', 'Kürşat', 'Yücel', 'Kubilay', 'Hayati', 'Bedrettin', 'Serdar', 'Serdan', 'Özgür', 'Fehmi', 'Fahrettin', 'Faik', 'İlhan', 'Ergün', 'Fatih', 'Serkan', 'Bahattin', 'Gökhan', 'Gürhan', 'Orhan', 'Berk', 'Umut', 'Özcan', 'Ata', 'Çetin', 'Turgay', 'Mehmet']

soyad = ['Şen','Kandemir','Çevik','Erkuran','Tüten','Öztürk','Yüzbaşıoğlu','Vural','Yücel','Sönmez','Ertekin','Dede','Uyanık','Aslan','Akbulut','Orhan','Uz','Yavuz','Erdem','Kulaç','Kaya','Selvi','Akpınar','Abacıoğlu','Çay','Işık','Özer','Özdemir','Demir','Öztürk']

grup = []
for i in range(500): 
    full_isim = random.choice(ad)+" "+random.choice(soyad)
    grup.append(full_isim)

cinsiyet = ['Erkek']

yas = []
for i in range(100):
    yas.append(i)



santiye = ['Teknopark Şantiyesi', 'Erasta Şantiyesi', 'Karaağaç Şantiyesi', 'Saraçlar Şantiyesi', 'Silivri Şantiyesi','Uşak Şantiyesi', 'Trabzon Şantiyesi', 'Karadeniz Şantiyesi', 'Bodrum Şantiyesi', 'Antalya Şantiyesi', 'Paris Şantiyesi', 'Makedonya Şantiyesi', 'Yunanistan Şantiyesi', 'Bulgaristan Şantiyes', 'Gebze Şantiyesi', 'Kocaeli Şantiyesi', 'Adıyaman Şantiyesi', 'Bursa Şantiyesi', 'Eskişehir Şantiyesi', 'Ankara Şantiyesi', 'İstanbul Şantiyesi', 'Edirne Şantiyesi']  



def Uret():
    for i in range(500):
		      p = Santiye.objects.get(isim = random.choice(santiye))
		      x = Personel(ad = random.choice(grup), cinsiyet = random.choice(cinsiyet), yas = random.choice(yas), baslamaTarih = datetime.datetime.now().date(), birim = p)
		      x.save()


```
