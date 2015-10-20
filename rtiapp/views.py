from django.shortcuts import render, render_to_response

def fblogintest(request):
	return render_to_response('fblogintest.html')

def logintest(request):
    return render_to_response('login/login.html')
# Create your views here.
