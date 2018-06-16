from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^user/', include('myapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/admin/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]