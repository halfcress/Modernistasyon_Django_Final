from django import forms



class Odemeislemi(forms.Form):
    hakediş_Proje = forms.CharField(max_length=30)
    hakediş_Santiye = forms.CharField(max_length=30)
    miktar = forms.CharField(max_length=30)
    tarih = forms.CharField()
    sebep = forms.CharField(max_length=100)