from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email',max_length=200, help_text='Required')
    # permission = models.CharField(max_length=30, blank=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email'  )


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                field.widget = forms.TextInput(attrs={'placeholder': field.label})



