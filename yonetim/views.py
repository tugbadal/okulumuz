# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import *
from yonetim.models import *
from yonetim.forms import *
from django.template import RequestContext

# Create your views here.

def ogretim_elemanlari_listesi(request):
    ogretim_elemanlari = OgretimElemani.objects.all()
    return render_to_response('ogretim_elemanlari_listesi.html', locals())

def ogretim_elemani_ekleme(request):
    if request.method == 'POST':
        form = OgretimElemaniFormu(request.POST)
        if form.is_valid():
            temiz_veri = form.cleaned_data
            ogrelm = OgretimElemani(adi=temiz_veri['adi'], soyadi=temiz_veri['soyadi'], telefonu=temiz_veri.get('telefonu'),
                e_posta_adresi=request.POST.get('e_posta_adresi'))
            ogrelm.save()
            return HttpResponseRedirect('/ogretim-elemanlari-listesi/')
        else:
            form = OgretimElemaniFormu()
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