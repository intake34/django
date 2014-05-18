from django import forms
from django.utils.safestring import mark_safe
from django.db import connection, transaction

from hotels.models import Hotel

class FeedbackForm(forms.Form):
	
	Hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(),required=True,label=mark_safe("<br/>Choose Hotel<br/>"))
	feedback = forms.CharField(required=True,label=mark_safe("<br/>FeedBack<br/>"))
	
