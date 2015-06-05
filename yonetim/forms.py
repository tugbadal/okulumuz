# -*- coding: utf-8 -*-
from django import forms


class OgretimElemaniFormu(forms.Form):
    adi = forms.CharField(label="Adı", required=True)
    soyadi = forms.CharField(label="Soyadı", required=True)
    telefonu = forms.CharField(label="Telefon Numarası", required=False)
    e_posta_adresi = forms.EmailField(label="E Posta Adresi", required=False)

    def clean_e_posta_adresi(self):
        adres = self.cleaned_data['e_posta_adresi']
        if '@' in adres:
            (kullanici, alan) =adres.split('@')
            if kullanici in ('root', 'admin', 'administrator'):
                raise forms.ValidationError('Bu adres geçersiz')
        return adres





