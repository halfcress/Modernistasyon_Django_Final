from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.anasayfa, name="anasayfa"),
    path('hakedis', views.Odeme, name='Odemeislemi'),
    path('personel', views.personel, name="personel"),
    path('santiye', views.santiye, name="santiye"),
    path('firma', views.firma, name="firma"),
    path('hakedis', views.hakedis, name="hakedis"),
    #path('index', views.index),

]