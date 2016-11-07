from django.conf.urls import include, url
from django.contrib import admin

# from app import views
from django.conf.urls import include, url
# from django.contrib.staticfiles.views import serve
from django.contrib import admin
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^app', include('field_of_experiments.urls')),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('homepage.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^static/(?P<path>.*)$', serve),
    # url(r'^media/(?P<path>.*)$', serve, {
    #     'document_root': settings.MEDIA_ROOT,
    # }),
]

