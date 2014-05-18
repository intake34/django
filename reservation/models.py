from django.db import models
from rooms.models import Room
from users.models import User

class Reservation(models.Model):
	fromdate = models.DateTimeField('start date')
	todate = models.DateTimeField('end date')
	user = models.ForeignKey(User)
	
class ReservationDesc(models.Model):
	no_of_rooms = models.IntegerField()
	room = models.ForeignKey(Room)
	res = models.ForeignKey(Reservation)
	
