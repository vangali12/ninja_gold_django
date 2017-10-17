# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from random import randint
from time import gmtime, strftime

# Create your views here.
def index(request):
	return render(request, 'ninjaGold_app/index.html')

def process(request):
	if request.POST['building'] == "farm":
		curGold = randint(10, 20)
		location = 'farm'
	elif request.POST['building'] == "cave":
		curGold = randint(5, 10)
		location = 'cave'
	elif request.POST['building'] == "house":
		curGold = randint(2, 5)
		location = 'house'
	elif request.POST['building'] == "casino":
		curGold = randint(-50, 50)
		location = 'casino'
	
	if 'curTotal' not in request.session:
		request.session['curTotal'] = curGold
	else:
		request.session['curTotal'] += curGold

	context = {
	'curGold': curGold,
	'location': location,
	'date': strftime("%x", gmtime()),
	'time': strftime("%X", gmtime()),
	}

	if 'arr' not in request.session:
		request.session['arr'] = []
		x = request.session['arr']
		x.append(context)
		request.session['arr'] = x
	else:
		x = request.session['arr']
		x.insert(0, context)
		request.session['arr'] = x
	print(request.session['arr'])

	return redirect("/")

def clear(request):
	request.session.clear()
	return redirect('/')