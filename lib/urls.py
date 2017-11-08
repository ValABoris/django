from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

import library.views

urlpatterns = [
    url(r'^$', library.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^library/', include('library.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)