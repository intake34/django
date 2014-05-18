from django.db import models
from django.forms import ModelForm
from django import forms

class User(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=32)
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.password
	def __unicode__(self):
		return self.name
		
		
		
	
	
