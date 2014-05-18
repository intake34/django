from django.db import models
from django.forms import ModelForm
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class Country(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=200)
	country_id = models.ForeignKey(Country)
	def __unicode__(self):
		return self.name
		
class Region(models.Model):
	name = models.CharField(max_length=200)
	city_id = models.ForeignKey(City)
	def __unicode__(self):
		return self.name
			
class Hotel(models.Model):
	name = models.CharField(max_length=200)
	country_id = models.ForeignKey(Country)
	city_id = models.ForeignKey(City)
	region_id = models.ForeignKey(Region)
	def __unicode__(self):
		return self.name

class HotelPic(models.Model):
	picture=models.ImageField(upload_to='images/')
	hotel_id = models.ForeignKey(Hotel)
	
class SearchHotelForm(ModelForm):
	class Meta:
		model = Hotel	
		


@receiver(pre_delete, sender=HotelPic)
def hotelpic_delete(sender, instance, **kwargs):
	instance.picture.delete(False)
