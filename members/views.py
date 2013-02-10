from members.models import Member, MemberManager
from members.forms import RegistrationForm, LoginForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

import json

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
    pass

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