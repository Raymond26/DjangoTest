from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoTest.views.home', name='home'),
    # url(r'^DjangoTest/', include('DjangoTest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^members/', include('members.urls', namespace="members")),
    url(r'^signup/', 'members.views.registration', name='signup'),
    url(r'^login/', 'members.views.loginRequest', name='login'),
    url(r'^logout/', 'members.views.logoutRequest', name='logout'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
