from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

def fblogintest(request):
	return render_to_response('fblogintest.html')

def logintest(request):
    return render_to_response('Login/login.html')

def base(request):
    return render_to_response('base.html')

@login_required
def home(request):
    return render_to_response('Home/home.html')
