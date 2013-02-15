from models import UserGallery
from django.shortcuts import render
from members.models import Member

def member_main_gallery(request, member_id):
    member = Member.objects.get(pk=member_id)
    return render(request, 'galleries/main_member_gallery.html', {
        'member': member,
        'gallery': member.main_gallery
    })