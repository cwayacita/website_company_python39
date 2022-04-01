from django.shortcuts import render
import pandas as pd


# Create your views here.

from django.shortcuts import render

from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

from django.contrib.auth.decorators import login_required
from .forms import ParkingForm, SearchDateForm
from .models import ModelParking, SearchDate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from datetime import datetime, timedelta

@login_required(login_url='/accounts/login/')
def parking_request(request):
    parking_data = ModelParking.objects.filter(parking_day_date=datetime.now().strftime("%Y-%m-%d")).first()
    parking_data2 = parking_data
    if request.method == 'POST' :
        if 'new_event' in request.POST:
            form = ParkingForm(request.POST)
            form2 = SearchDateForm()

            if form.is_valid():
                parking_new = form.save()
            return render(request, 'parking/index.html', {'form': form, 'form2': form2, 'parking_data': [
                parking_data],'parking_data2': [
                parking_data2]})  # ,'parking_data': parking_data


        elif 'search_date' in request.POST:
            form2 = SearchDateForm(request.POST)
            form = ParkingForm(initial={'user_name': request.user})
            date_time_obj = datetime.strptime(request.POST.get('search_day_date'), "%Y-%m-%d")
            date_time_obj = date_time_obj.strftime("%Y-%m-%d")
            # parking_data = ModelParking.objects.filter(parking_day_date=date_time_obj)
            # parking_data = ModelParking.objects.all()
            parking_data2 = ModelParking.objects.filter(parking_day_date=date_time_obj).first()

            # return render(request, 'parking/index.html' , {'form2': form2,'parking_data': [parking_data], 'date_time_obj': [date_time_obj]}) #,'parking_data': parking_data
            return render(request, 'parking/index.html', {'form': form, 'form2': form2, 'parking_data': [
                parking_data],'parking_data2': [
                parking_data2]})  # ,'parking_data': parking_data


    elif request.method == 'GET':
        form = ParkingForm(initial={'user_name': request.user})
        form2 = SearchDateForm()

    # parking_data = ModelParking.objects.order_by('-input_date').first
        return render(request, 'parking/index.html', {'form': form, 'form2': form2, 'parking_data': [
            parking_data], 'parking_data2': [
            parking_data2]})  # ,'parking_data': parking_data








