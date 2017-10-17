from django.conf.urls import url
from django.contrib import admin

from . import views

def test(request):
	print """


	app level test


	"""

urlpatterns = [
	url(r'^$', views.index),
	url(r'^process_money$', views.process),
	url(r'^clear$', views.clear),
]