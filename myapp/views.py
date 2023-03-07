from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import * #tek tek uğraşmamak adına her şeyi import ettim.
from .forms import * #tek tek uğraşmamak adına her şeyi import ettim.
from django.contrib.auth.decorators import login_required
from django.db import transaction
import decimal
from django.shortcuts import render
from django.http import HttpResponseRedirect
import decimal
from django.db import transaction


@login_required(login_url='/account/login') #@login_required login olmadan giriş yapılamaması için her sayfaya eklendi.
def anasayfa(request):
    anasayfa = Sirket.objects.order_by("-isim")

    context = {
        "anasayfa": anasayfa,
    }

    return render(request, 'myapp/index.html', context)

@login_required(login_url='/account/login')
def personel(request):

    personel = Personel.objects.all().order_by('id')

    context = {
        "personel" : personel,
    }
    
    return render(request, 'myapp/personel.html', context)

@login_required(login_url='/account/login')
def santiye(request):
    santiye = Santiye.objects.all().prefetch_related('personel_set').order_by('id')
    

    context = {
        "santiye" : santiye,
    }
    
    return render(request, 'myapp/santiye.html', context)

@login_required(login_url='/account/login')
def firma(request):
    sirket = Sirket.objects.all().prefetch_related('proje_set__santiye_set__personel_set').order_by('id')
    #santiye = Sirket.objects.all().prefetch_related('proje_set__santiye_set').order_by('id')
    #deneme = Sirket.objects.filter(id__in=Proje(santiye.values('id')))

    context = {
        "sirket" : sirket,
        #"santiye" : santiye,
        #"deneme" : deneme,
    }
        
    return render(request, 'myapp/firma.html', context)

@login_required(login_url='/account/login')
def hakedis(request):

    sirket = Sirket.objects.all().prefetch_related('proje_set__santiye_set__personel_set').order_by('id')
    #santiye = Sirket.objects.all().prefetch_related('proje_set__santiye_set').order_by('id')
    #deneme = Sirket.objects.filter(id__in=Proje(santiye.values('id')))

    context = {
        "sirket" : sirket,
        #"santiye" : santiye,
        #"deneme" : deneme,
    }

    return render(request, 'myapp/hakedis.html', context)

@login_required(login_url='/account/login')
def Odeme(request): 

  if request.method == 'POST':

    form = Odemeislemi(request.POST)

    if form.is_valid():

      x = form.cleaned_data['hakediş_Proje']
      y = form.cleaned_data['hakediş_Santiye']
      z = decimal.Decimal(form.cleaned_data['miktar'])
      tarih = form.cleaned_data['tarih']
      sebep = form.cleaned_data['sebep']

      odeyen = Proje.objects.select_for_update().get(ad = x)
      odemeyiAlan = Santiye.objects.select_for_update().get(isim = y)
      

    with transaction.atomic():
      odeyen.miktar -= z
      odeyen.save()

      odemeyiAlan.miktar += z
      odemeyiAlan.save()
    
      tarih = Tarih(tarih=tarih, aciklama=sebep, odenen_proje= x, odenen_santiye=y, odenen_tutar = z) #Class ismi tarih olması yanıltmasın, bütün bilgileri çektiğim bir class oluşturdum ayriyetten.
      tarih.save()
      

      return HttpResponseRedirect('/anasayfa/hakedis')

  else:
    form = Odemeislemi()
    

    tarih = Tarih.objects.all()

  return render(request, 'myapp/hakedis.html', {'form': form, "tarih":tarih}) #tek bir form ve tek bir değişken ile context göndererek 