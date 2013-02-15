from django.conf.urls import patterns, url

urlpatterns = patterns('',
    #url(r'^$', 'members.views.index', name='index'),
    #url(r'^json/$', 'members.views.members_json', name='members_json'),
    url(r'^member/(?P<member_id>\d+)/$', 'galleries.views.member_main_gallery', name='member_main_gallery'),
    #url(r'^avatar_upload/$', 'members.views.upload_avatar', name='upload_avatar'),
    #url(r'^upload_image/$', 'members.views.upload_image', name='upload_image'),
)