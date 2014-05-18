from django.db import models
from django.contrib.auth.models import User
from rooms.models import Hotel

class Feedback(models.Model):
	message = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	hotel_id = models.ForeignKey(Hotel)
	def __unicode__(self):
		return self.message
	
