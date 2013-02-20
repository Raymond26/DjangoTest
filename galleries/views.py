from models import UserGallery
from django.shortcuts import render
from members.models import Member
from galleries.models import UserGallery, ImageModel, PhotoCommentTree

def member_main_gallery(request, member_id):
    member = Member.objects.get(pk=member_id)
    return render(request, 'galleries/main_member_gallery.html', {
        'member': member,
        'gallery': member.main_gallery
    })

def public_member_gallery(request, gallery_id):
    gallery = UserGallery.objects.get(pk=gallery_id)
    member = Member.objects.get(pk=gallery.owner_id)
    return render(request, 'galleries/public_member_gallery.html', {
        'member': member,
        'gallery': gallery
    })

def public_member_photo(request, gallery_id, photo_id):

    gallery = UserGallery.objects.get(pk=gallery_id)
    member = Member.objects.get(pk=gallery.owner_id)
    photo = ImageModel.objects.get(pk=photo_id)
    photo.view_count += 1
    photo.save()

    return render(request, 'galleries/public_member_photo.html', {
        'member': member,
        'gallery': gallery,
        'photo': photo,
    })