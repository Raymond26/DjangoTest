from django.conf.urls import patterns, url

from members.models import Member

urlpatterns = patterns('',
    url(r'^$', 'members.views.index', name='index'),
    url(r'^json/$', 'members.views.members_json', name='members_json'),
    url(r'^id/(?P<member_id>\d+)/$', 'members.views.detail_member', name='detail'),
    url(r'^avatar_upload/$', 'members.views.upload_avatar', name='upload_avatar'),
    url(r'^upload_image/$', 'members.views.upload_image', name='upload_image'),
)