# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length = 30, blank = True, null = True)
	pic = models.ImageField(upload_to = 'users' ,blank = True, null=True)

	def __unicode__(self):
		return self.user.username
