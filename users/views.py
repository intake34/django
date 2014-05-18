from django.shortcuts import render
from users.models import User
from django import forms
from users.forms import ContactForm , RegisterForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.models import User

def index(request):
	if not request.user.is_authenticated():
		if request.method == 'POST':
			form = ContactForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
			else:
				messages.error(request, "Error")	
		
		else:
			form = ContactForm(label_suffix='')
		return render(request,'users/index.html',{'form': form})
	else:
		return render(request,'users/index.html',{'form': "Wlecomeback"})
		
		
def login(request):
	name = request.POST['e_mail']
	passs = request.POST['password']
	user = authenticate(username=name, password=passs)
	if user is not None:
		if user.is_active:
			auth_login(request,user) 
			return render(request,'users/index.html',{'form': "Welcome"})    
		else:
			return render(request,'users/index.html',{'form': "disabled "})
	else:
		return render(request,'users/index.html',{'form': name})
	return render(request,'users/index.html',{'form': name})
	
	
def logout(request):
	auth_logout(request)
	return render(request,'users/index.html',{'form': "logged out"})
	
def register(request):
	if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				name = request.POST['user']
				passs = request.POST['password']
				email = request.POST['e_mail']
				try:
					u = User.objects.get(username=name)
					return render(request,'users/register.html',{'form': "sorry this user is already exist"})
				except:
					user = User.objects.create_user(email, name , passs)
					user.save()
					return render(request,'users/register.html',{'form': "added successfully"})
			else:
				messages.error(request, "Error")	
				return render(request,'feedbacks/add.html',{'form': form,'message':" !"})
	else:
			form = RegisterForm(label_suffix='')
	return render(request,'users/register.html',{'form': form})
	
		
