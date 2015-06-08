# -*- coding: utf-8 -*-
from django import forms


class OgretimElemaniFormu(forms.Form):
    adi = forms.CharField(label="Adı")
    soyadi = forms.CharField(label="Soyadı")
    telefonu = forms.CharField(label="Telefon Numarası", required=False)
    e_posta_adresi = forms.EmailField(label="E Posta Adresi", required=False)

    def clean_e_posta_adresi(self):
        adres = self.cleaned_data['e_posta_adresi']
        if '@' in adres:
            (kullanici, alan) =adres.split('@')
            if kullanici in ('root', 'admin', 'administrator'):
                raise forms.ValidationError('Bu adres geçersiz')
        return adres

    def clean_soyadi(self):
        soyad = self.cleaned_data['soyadi']
        if not soyad:
            raise forms.ValidationError('soyadı alanı gerekli')
        return soyad



