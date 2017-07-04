# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models  import User
from django.db import models

# Create your models here.

class blog(models.Model):
	username = models.ForeignKey(User)
	picture = models.ImageField(upload_to = 'pictures', blank = True, null = True)
	title = models.CharField(max_length = 30)
	content = models.TextField()
	date = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.title
	

	# class Meta:
	# 	ordering=['-date']
	# either this or what i have done in view.py