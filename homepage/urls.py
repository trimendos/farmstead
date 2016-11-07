from django.conf.urls import url, include
from django.views.static import serve
from django.contrib import admin
from .views import index

from django.conf import settings

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^admin/', admin.site.urls),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #     {'document_root': settings.MEDIA_ROOT, }),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^$', page, name='homepage'),
    # url(r'^(?P<slug>[\w./-]+)/$', page, name='page'),

    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^static/(?P<path>.*)$', serve),
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),

]
