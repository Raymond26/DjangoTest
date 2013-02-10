from django.conf.urls import patterns, url

from members.models import Member

urlpatterns = patterns('',
    url(r'^$', 'members.views.index', name='index'),
    url(r'^json/$', 'members.views.members_json', name='members_json'),
    url(r'^id/(?P<member_id>\d+)/$', 'members.views.detail_json', name='detail_json'),
)