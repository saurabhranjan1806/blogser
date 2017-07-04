# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.shortcuts import render
from django.http import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
from .forms import *
from .models import *
from blogser.views import *
from django.contrib.auth.models  import User
# Create your views here.

def index(request):
	if request.user.is_authenticated():			#good concept to cut the urls from the end like(loggedIn etc)
		return loggedIn(request)
	form = RegForms()
	return render(request, 'login/home.html', {'form' : form})


def auth_view(request):
	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		auth.login(request, user)
	else:
		return HttpResponseRedirect('/invalid/')
	return HttpResponseRedirect('/loggedIn/')


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')


def register(request):
	if request.method=="POST":
		form = RegForms(request.POST)
		if form.is_valid():
			# form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password1')
			User.objects.create_user(username=username, password=password, email=email)
			return render(request, 'login/register_success.html', {'name': request.POST['username']})
			# return HttpResponseRedirect('/')
	else:
		form = RegForms()
	return render(request, 'login/register.html', {'form':form})


# def loggedIn(request):
#     if request.user.is_authenticated():
#         return render(request,'login/login.html',{'fullname':request.user.username})
#     else:
#         return HttpResponseRedirect('/')