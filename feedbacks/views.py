from django.shortcuts import render
from feedbacks.forms import FeedbackForm
from feedbacks.models import Feedback
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import connection, transaction
from django.contrib.auth.decorators import login_required 
@login_required
def index(request):
		form = FeedbackForm()	
		if request.method == 'POST':
			#if form.is_valid():
				hotelid = request.POST.get('Hotel',False)
				feedback = request.POST['feedback']
				cursor = connection.cursor()
		 		cursor.execute("select distinct h.id,h.name"
					" from rooms_room as r,reservation_reservation as res,"
					" reservation_reservationdesc as resdesc,hotels_hotel as h ,"
					" rooms_roomtype as type"
					" where res.id = resdesc.res_id and resdesc.room_id = r.id and res.user_id= %s "
					" and type.id = r.room_type_id", [request.user.id])
					
				exist = cursor.fetchall()
				if exist:
					feed = Feedback.objects.create(message=feedback,user_id=request.user.id,hotel_id_id=hotelid)
					feed.save()
					return render(request,'feedbacks/add.html',{'form': form,'message':"Thanks sir !",'username':request.user})
				else:
					return render(request,'feedbacks/add.html',{'form': form,'message':"sorry you didn't check in before !",'username':request.user})
			#else:
				messages.error(request, "Error")			
				return render(request,'feedbacks/add.html',{'form': "ERROR",'username':request.user})
		else:		
			return render(request,'feedbacks/add.html',{'form': form,'username':request.user})
