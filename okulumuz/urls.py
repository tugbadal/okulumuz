from django.conf.urls import patterns, include, url
import yonetim.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'okulumuz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ogretim-elemanlari-listesi/', yonetim.views.ogretim_elemanlari_listesi),
    url(r'^get-deneme/', yonetim.views.get_deneme),
    url(r'^ogretim-elemani-ekleme/', yonetim.views.ogretim_elemani_ekleme),

)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()