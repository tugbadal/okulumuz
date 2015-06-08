# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import *
from yonetim.models import *
from yonetim.forms import *
from django.template import RequestContext
from django.core.paginator import Paginator

# Create your views here.

def ogretim_elemanlari_listesi(request):
    siralama = 'soyadi'
    olcut = request.GET.get('sirala')
    sayfa = request.GET.get('sayfa',1)
    if olcut:
        siralamaOlcutleri = {'1':'adi', '2':'soyadi', '3':'e_posta_adresi'}
        if olcut in siralamaOlcutleri:
            siralama = siralamaOlcutleri[olcut]
    ogretim_elemanlari_tumu = OgretimElemani.objects.order_by(siralama)
    ogretim_elemanlari_sayfalari = Paginator(ogretim_elemanlari_tumu, 5)
    ogretim_elemanlari = ogretim_elemanlari_sayfalari.page(int(sayfa))
    return render_to_response('ogretim_elemanlari_listesi.html', locals())

def ogretim_elemani_ekleme(request):
    ogrelmID = request.GET.get('id')
    if ogrelmID:
        try:
            ogrelm = OgretimElemani.objects.get(id=ogrelmID)
        except:
            return HttpResponse(u'aradıgınız öğretim elemanı bulunamıyor: ID=%s' %ogrelmID)
    if request.GET.get('sil'):
        OgretimElemani.objects.get(id=ogrelmID).delete()
        return HttpResponseRedirect('/ogretim-elemanlari-listesi/')

    if request.method == 'POST':
        form = OgretimElemaniFormu(request.POST)
        if form.is_valid():
            temiz_veri = form.cleaned_data
            if not ogrelmID:
                ogrelm = OgretimElemani(adi=temiz_veri['adi'], soyadi=temiz_veri['soyadi'], telefonu=temiz_veri.get('telefonu'),
                    e_posta_adresi=request.POST.get('e_posta_adresi'))
                ogrelm.save()
                return HttpResponseRedirect('/ogretim-elemanlari-listesi/')
            else:
                if ogrelmID:
                    ogrelm = OgretimElemani.objects.get(id=ogrelmID)
                    form = OgretimElemaniFormu(initial=ogrelm.__dict__)
                else:
                    form = OgretimElemaniFormu()
                    return render_to_response('genel_form.html', {'form':form, 'baslik': 'Öğretim elemanı ekleme', 'ID':ogrelmID},
                                                      context_instance=RequestContext(request))
        else:
            return render_to_response('genel_form.html', {'form':form, 'baslik': 'Öğretim elemanı ekleme'},
                                              context_instance=RequestContext(request))
    else:
        form = OgretimElemaniFormu()
        return render_to_response('genel_form.html', {'form':form, 'baslik': 'Öğretim elemanı ekleme'},
                                      context_instance=RequestContext(request))




        """
        adi = request.POST.get('adi')
        soyadi = request.POST.get('soyadi')
        telefonu = request.POST.get('telefonu')
        e_posta_adresi = request.POST.get('e_posta_adresi')
        hatalar = []
        if not (adi and soyadi):
            hatalar.append(u'adı ve soyadı alanlarının doldurulması zorunludur!')
        if e_posta_adresi:
            if not '@' in e_posta_adresi:
                hatalar.append('e posta adresi yanlıs')
        if not hatalar:
            ogrelm = OgretimElemani(adi=adi, soyadi=soyadi, telefonu=telefonu, e_posta_adresi=e_posta_adresi)
            ogrelm.save()
            return HttpResponse(u'''<h2>Aşağıdaki öğretim elemanı eklendi </h2>
            <br><b>Adı:</b>%s
            <br><b>Soyadı:</b>%s
            <br><b>Telefonu:</b>%s
            <br><b>E-Posta Adresi:</b>%s''' %(adi, soyadi, telefonu, e_posta_adresi))
        else: return render_to_response('yonetim/ogretim_elemani_formu.html', locals(), context_instance=RequestContext(request))
    else:
        return render_to_response('yonetim/ogretim_elemani_formu.html',locals(), context_instance=RequestContext(request))
        """
def get_deneme(request):
    if request.method == 'GET':
        adi = request.GET['adi']
        soyadi = request.GET['soyadi']
        return HttpResponse(u'<b>Adı:</b> %s <br><b>Soyadı:</b>%s' %(adi, soyadi))

    else:
        pass