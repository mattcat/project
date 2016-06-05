from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (authenticate,get_user_model,login,logout)
from .forms import UserLoginForm, UserRegistrationForm
# Create your views here.

def login_view(request):
	# print request.user.is_authenticated()
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		login(request, user)
		print request.user.is_authenticated()
		messages.add_message(request, messages.INFO, 'Hello '+username)
		if next:
			return redirect(next)
		return redirect("/")    
	context = {
		"title" : "Login",
		"form" : form, 
	}
	return render(request, "form.html", context)

def logout_view(request):
	title = "Logout"
	logout(request)
	return redirect("/")  

def register_view(request):
	# print request.user.is_authenticated() 
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username,password=password)
		login(request, new_user)
		return redirect("/")

	context = {
		"title" : "Register",
		"form" : form, 
	}
	return render(request, "form.html", context)