"""djangomenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf.urls.static import static
from menu.views import TilesView, TileDetailView, IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'^root_tiles/$', TilesView.as_view()),
    url(r'^tile_detail/(?P<pk>\w+)/$', TileDetailView.as_view(), name="tile-detail"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += patterns('django.views.static',
                        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
                        )
