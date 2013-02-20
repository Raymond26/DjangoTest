from members.models import Member, MemberManager
from members.forms import RegistrationForm, LoginForm, AvatarUploadForm, ImageUploadForm
from galleries.models import ImageModel
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from PIL import Image

import json
import StringIO

def index(request):
    # Returning all objects for now.. too much data being sent, will fix later
    return render(request, 'members/index.html', {'members': Member.objects.all()})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            member = Member.objects.create_user(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password"),
                email=form.cleaned_data.get("email"))
            member.location = form.cleaned_data.get("location")
            member.save()
            return HttpResponseRedirect('/members/')
        else:
            return render(request, 'members/signup.html', {'form':form})
    else:
        form = RegistrationForm()
        return render(request, 'members/signup.html', {'form': form})

def loginRequest(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            member = authenticate(username=username, password=password)
            if member is not None:
                login(request,member)
                return HttpResponseRedirect('/members/')
            else:
                return render(request, 'members/login.html', {'form':form})
        else:
            return render(request, 'members/login.html', {'form':form})
    else:
        form = LoginForm()
        return render(request, 'members/login.html', {'form': form})

def logoutRequest(request):
    logout(request)
    return HttpResponseRedirect('/members/')

def detail_member(request, member_id):
    member = Member.objects.get(pk=member_id)
    avatar_upload_form = AvatarUploadForm()
    image_upload_form = ImageUploadForm()
    return render(request, 'members/detail.html', {
        'member': member,
        'avatar_upload_form': avatar_upload_form,
        'image_upload_form': image_upload_form,
    })

def upload_avatar(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            avatar_upload_form = AvatarUploadForm(request.POST, request.FILES)
            if avatar_upload_form.is_valid:
                member = Member.objects.get(username=request.user.username)
                member.avatar_pic = request.FILES['file']
                member.save()
            return HttpResponseRedirect(reverse('members:detail', kwargs={
                'member_id': request.user.pk
            }))

        else:
            return HttpResponseRedirect(reverse('members:detail', kwargs={
                'member_id': request.user.pk
            }))
    else:
        return HttpResponseRedirect(reverse('login'))

def upload_image(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            image_upload_form = ImageUploadForm(request.POST, request.FILES)
            if image_upload_form.is_valid:

                image = request.FILES['image']
                thumb_io = StringIO.StringIO()
                size = 256, 256
                thumbnail = Image.open(image)
                thumbnail.thumbnail(size, Image.ANTIALIAS)
                thumbnail.save(thumb_io,format='JPEG')
                thumb_file = InMemoryUploadedFile(thumb_io, None, image.name, image.content_type, thumb_io.len, None)

                member = Member.objects.get(pk=request.user.pk)
                image_model = ImageModel(
                    image=image,
                    description=request.POST['description'],
                    filesize=image.size,
                    owner=member,
                    thumbnail=thumb_file
                )
                image_model.save()

                member.main_gallery.add_photo(image_model)
                member.save()

            return HttpResponseRedirect(reverse('members:detail', kwargs={
                'member_id': request.user.pk
            }))
        else:
            return HttpResponseRedirect(reverse('members:detail', kwargs={
                'member_id': request.user.pk
            }))
    else:
        return HttpResponseRedirect(reverse('login'))


def members_json(request):
    member_list = [member.get_username_with_id() for member in Member.objects.all()]
    return HttpResponse(json.dumps(member_list), content_type="application/json")

def detail_json(request, member_id):
    member = Member.objects.get(pk=member_id)
    if member.date_of_birth is None:
        date_of_birth = None
    else:
        date_of_birth = member.date_of_birth.isoformat()

    response = {
        'id' : member.pk,
        'email' : member.email,
        'username' : member.username,
        'location' : member.location,
        'date_of_birth' : date_of_birth,
    }
    return HttpResponse(json.dumps(response), content_type="application/json")