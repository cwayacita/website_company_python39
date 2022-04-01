from django.urls import path
# from .views import input_tasks
from .views import simple_upload,  simple_upload_validated
from django.conf.urls import url
app_name = 'form'

#one url in this projectcontaining table, form and filtered task accessible at http://127.0.0.1:8000/form/form_output/
urlpatterns = [
    # path('form_output/', input_tasks),
    path('media/', simple_upload,  name='simple_upload'),
    # path('media/link', reload,  name='reload'),
    path('media/validated/', simple_upload_validated,  name='simple_upload_validated'),
    # path('media/validated/link', reload_validated, name='reload_validated'),

]