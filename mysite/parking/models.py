from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.conf import settings

class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True

class ModelParking(models.Model):
    free_places_parking = models.CharField(max_length=200,
                                           help_text="How many parking available you have seen"
                                           )
    input_date = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d %H:%M"),
                                  help_text="Date Event", editable=False
                                  )
    parking_day_date = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d"),
                                            help_text="Please pick up the date",
                                            )
    user_name = models.CharField(max_length=200, default='cwayacita', help_text="Your user", editable=False)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    class Meta:
        ordering = ('-input_date',)

class SearchDate(models.Model):
    search_day_date = models.DateTimeField(default=datetime.now().strftime("%Y-%m-%d"),
                                            help_text="Please pick up the date",
                                            )
    class Meta:
        ordering = ('search_day_date',)





