from django.shortcuts import render
from hotels.forms import SearchHotelForm
from hotels.models import Hotel , HotelPic
from feedbacks.models import Feedback
from django.contrib import messages 
from django.db import connection, transaction
from django.http import HttpResponseRedirect
   # Create your views here.
def index(request):
	form = SearchHotelForm()
	return render(request,'hotels/search.html',{'form': form,'username':request.user})
	
def search(request):
	if request.method == 'POST':
		if request.user.is_authenticated:
			form = SearchHotelForm(request.POST)
			if form.is_valid():
				cd = form.cleaned_data
				cityid = request.POST.get('city', False)
				country = request.POST['country']
				region = request.POST['region']
				hotel = request.POST['hotel']
				fromdate = request.POST['fromdate']
				todate = request.POST['todate']
				q=Hotel.objects.filter(name=hotel).filter(country_id=country).values('name','id')
				
				if not q:
					return render(request,'hotels/search.html',{'form': form,'message':"there is no hotel with that name",'username':request.user})
				else:
					cursor = connection.cursor()
					
 					cursor.execute("select r.*,rt.description from rooms_room as r , rooms_roomtype as rt"
					 " where r.room_type_id = rt.id and r.hotel_id =%s and r.id not in(select  distinct room_id"
					" from reservation_reservation as res,"
					 " reservation_reservationdesc as resdesc,hotels_hotel as h" 
					 " where res.id = resdesc.res_id "
					 " and (res.fromdate   between %s and %s"
					 " and res.todate   between %s and %s))"
						, [q[0]['id'],fromdate,todate,fromdate,todate])
					
					rooms = cursor.fetchall()
					pic = HotelPic.objects.filter(hotel_id_id=q[0]['id']).values('picture')
					feedbacks = Feedback.objects.filter(hotel_id_id=q[0]['id']).values('message')
					return render(request,'hotels/show.html',{'rooms': rooms,'pic':pic,'fromdate':fromdate,'todate':todate,'feeds':feedbacks,'username':request.user})
					
			else:
				messages.error(request, "Error")	
		else:
			return HttpResponseRedirect("/users/")
	else:
			form = SearchHotelForm(label_suffix='')
	return render(request,'hotels/search.html',{'form': form})

