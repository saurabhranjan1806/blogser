# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.shortcuts import render
from django.http import *
from django.contrib.auth.models  import User
from .forms import *
from .models import *
from django.db.models import *
# Create your views here.

def loggedIn(request):
	if request.user.is_authenticated():
		if request.method=="POST":
			form = blogForm(request.POST, request.FILES)
			if form.is_valid:
				f = form.save(commit = False)		#imp concept
				f.username = request.user
				f.save()
				return HttpResponseRedirect('/loggedIn/')
		else:
			form = blogForm()
			# form.username = request.user.username
			n = blog.objects.all().order_by('-date')
		return render(request,'blogser/home.html',{'fullname':request.user.username, 'form': form, 't':n})
	else:
		return HttpResponseRedirect('/')

@login_required
def delete(request,d):
    n = blog.objects.get(id=d)
    n.delete()
    return HttpResponseRedirect('/loggedIn/')

@login_required
def search(request):
	if request.method == 'POST':
		squery = request.POST['search_box']
		if squery:
			s = blog.objects.filter(Q(title__icontains=squery) |Q(content__icontains=squery) |Q(username__username__exact=squery))
			if s:
				return render(request,'blogser/home.html',{'fullname':request.user.username,'t':s})
        	else:
        		return render(request,'blogser/home.html')
       	else:
       		return HttpResponseRedirect('/logged_in/')