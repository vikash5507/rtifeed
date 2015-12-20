from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def fblogintest(request):
	return render_to_response('fblogintest.html')

@login_required
def logintest(request):
    return render_to_response('Login/login.html')

@login_required
def base(request):
    return render_to_response('base.html')

@login_required
def home(request):
    return render_to_response('Home/home.html')

@login_required
def getfeed(request):
    return render_to_response('Home/feedbox.html')

@login_required
def departmenttest(request):
	return render_to_response('Department/department.html')	