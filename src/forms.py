from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from src.models import BLog, Comment

from django import forms
from django.core.exceptions import ValidationError

User = get_user_model()

class FormCreateUser(UserCreationForm):
   class Meta:
    model = User
    fields=('username', 'email' , 'password1',  )


   def clean_email(self):
      email = self.cleaned_data.get('email')
      new = User.objects.filter(email=email)
      if new.count():
         raise ValidationError('Email Already Exist please create your acccounts with new email')

      return email   


class FormPost(forms.ModelForm):
   class Meta:
      model = BLog
      exclude = ['date']
      


      fields =['category', 'name', 'Text' ,'image'] 



   def clean_name(self):
      name = self.cleaned_data.get('name')
      if len(name) < 5:
         raise ValidationError('Name is shut  please and try with long name.')

      return name   



class FormComment(forms.ModelForm):
   class Meta :
      model = Comment

      fields = ['content']


 