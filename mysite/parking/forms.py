from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import ModelParking, SearchDate
from django.forms import ModelForm
from datetime import datetime, timedelta
from django.conf import settings
from django.contrib.auth.models import User

class ParkingForm(forms.ModelForm):
    class Meta:
        model = ModelParking
        fields='__all__'
        parking_day_date=forms.DateTimeField(input_formats=['%d/%m/%Y'], initial=datetime.now().strftime("%d/%m/%Y")) # %H:%M
        free_places_parking = forms.CharField(max_length=200, widget=forms.HiddenInput(), initial='How many places are free')
        input_date = forms.TimeField(input_formats=['%d/%m/%Y %H:%M'], initial=datetime.now().strftime("%d/%m/%Y %H:%M:%s"))
        user_name = forms.CharField(max_length=200, widget=forms.HiddenInput(), initial='test')

    def __init__(self, *args, **kwargs):
        super(ParkingForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget = forms.TextInput(attrs={'placeholder': field.label})

class SearchDateForm(forms.ModelForm):
    class Meta:
        model = SearchDate
        fields='__all__'
        search_day_date = forms.DateTimeField(input_formats=['%d/%m/%Y'], initial=datetime.now().strftime("%d/%m/%Y")) # %H:%M

    def __init__(self, *args, **kwargs):
        super(SearchDateForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget = forms.TextInput(attrs={'placeholder': field.label})




