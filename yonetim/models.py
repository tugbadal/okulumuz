from django.db import models

# Create your models here.
class OgretimElemani(models.Model):
    
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=50)
    telefonu = models.CharField(max_length=10, blank=True)
    e_posta_adresi = models.EmailField(blank=True)
    def __unicode__(self):
        return u'%s, %s' %(self.adi, self.soyadi)

class Ders(models.Model):
    kodu = models.CharField(max_length=10)
    adi= models.CharField(max_length=50)
    ogretim_elemani = models.ForeignKey(OgretimElemani)
    tanimi = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return u'%s,%s,%s,%s' %(self.kodu, self.adi, self.ogretim_elemani, self.tanimi)

class Ogrenci(models.Model):
    numarasi = models.IntegerField()
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=50)
    aldigi_dersler = models.ManyToManyField(Ders)

    def __unicode__(self):
        return u'%s,%s, %s, %s' %(self.numarasi, self.adi, self.soyadi, self.aldigi_dersler)