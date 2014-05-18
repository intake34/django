from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.models import User
import urlparse
from reservation.models import Reservation , ReservationDesc

def index(request):
	return render(request,'reservation/show.html',{'form': 'hey','username':request.user})    
def register(request):
	if request.user.is_authenticated():
		url = request.get_full_path()
		query = urlparse.urlparse(url).query
		params = urlparse.parse_qs(query)
		
		i=0
		res = Reservation.objects.create(fromdate=params['fromdate'][0], todate=params['todate'][0],user_id=1)
		res.save()
		
		for param in params['id']:
			if (params['no_of_rooms'][i] != "0" ):
				n = ReservationDesc.objects.create(no_of_rooms=params['no_of_rooms'][i], room_id=param,res_id=res.id)
				n.save()
				i+=1
			
		return render(request,'reservation/show.html',{'form': "your Reservation Completed :-)",'username':request.user})    
	else:
		return render(request,'reservation/show.html',{'form': "you need to sign in",'username':request.user})  

