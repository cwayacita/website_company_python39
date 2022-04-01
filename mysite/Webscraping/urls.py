from django.urls import path
from .views import simple_upload_web
app_name = 'Webscraping'

#one url in this projectcontaining table, form and filtered task accessible at http://127.0.0.1:8000/form/form_output/
urlpatterns = [
    # path('form_output/', input_tasks),
    path('excel/', simple_upload_web,  name='simple_upload_web'),
    # path('media/link', reload,  name='reload'),
    # path('media/validated/', simple_upload_validated,  name='simple_upload_validated'),
    # path('media/validated/link', reload_validated, name='reload_validated'),

]