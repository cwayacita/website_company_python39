from django.db import models
from datetime import datetime, timedelta


#
# class Task(models.Model):
#     task_text = models.CharField(max_length=200)
#     task_date = models.TimeField(default=datetime.now)
#     time_new = models.TimeField(default=(datetime.now() + timedelta(minutes=25) ))
#     is_finished = models.BooleanField(default=False)
#     begin_date = models.DateTimeField(default=datetime.now)
#
#     #prpearing the update of the time
#     @property
#     def archive_post(self):
#         if not self.is_finished:
#             self.is_archived = True
#             self.begin_date = datetime.now()
#             self.save()
#
# class Task2(models.Model):
#     is_finished = models.BooleanField(default=False)
#     begin_date = models.DateTimeField(default=datetime.now)
#
#     #prpearing the update of the time
#     @property
#     def archive_post(self):
#         if not self.is_finished:
#             self.is_archived = True
#             self.begin_date = datetime.now()
#             self.save()
#
#
