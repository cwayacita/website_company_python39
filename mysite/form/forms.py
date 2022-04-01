from django import forms


class task_form(forms.Form):
  task_name = forms.CharField(label='new Task input', max_length=100)


