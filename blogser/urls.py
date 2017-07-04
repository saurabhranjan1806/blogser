from django.conf.urls import url, include
from .views import *


urlpatterns = [
	url(r'^$', loggedIn),
	url(r'^delete/(\d+)/', delete, name = 'delete'),
	url(r'^search_query/$', search),

]