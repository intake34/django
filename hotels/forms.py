from django import forms
from django.utils.safestring import mark_safe
from hotels.models import Region
from hotels.models import City
from hotels.models import Country

class SearchHotelForm(forms.Form):
	
	hotel = forms.CharField(required=True,label=mark_safe("HotelName<br/>"))
	country = forms.ModelChoiceField(queryset=Country.objects.all(),required=True,label=mark_safe('<br/>Country<br/>'))
	City = forms.ModelChoiceField(queryset=City.objects.all(),required=True,label=mark_safe("<br/>City<br/>"))
	region = forms.ModelChoiceField(queryset=Region.objects.all(),required=True,label=mark_safe("<br/>region<br/>"))
	fromdate = forms.CharField(required=True,label=mark_safe("<br/>formDate<br/>"))
	todate = forms.CharField(required=True,label=mark_safe("<br/>ToDate<br/>"))
