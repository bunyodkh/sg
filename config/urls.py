from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/en/', permanent=True)),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('manage/', admin.site.urls),
    path('', include('space.urls')),
    path('registry/', include('registry.urls')),
    path('contribute/', include('contribute.urls')),
    prefix_default_language=True
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
