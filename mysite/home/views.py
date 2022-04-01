from django.shortcuts import render
import pandas as pd


# Create your views here.

from django.shortcuts import render

from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

from django.contrib.auth.decorators import login_required



@login_required(login_url='/accounts/login/')
def home(request):


    return render(request , 'home/index.html' )