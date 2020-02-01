from django import forms
from .models import User

class UserForm(forms.ModelForm):
  fname=forms.CharField(label='first name :',widget=forms.TextInput(attrs ={"placeholder " : "First Name..."}))
  lname=forms.CharField(label='last name  :',widget=forms.TextInput(attrs ={"placeholder " : "Last Name...."}))
  email=forms.CharField(label='email :',widget=forms.TextInput(attrs ={"placeholder " : "email..."}))
  password=forms.CharField(label='password :',widget=forms.TextInput(attrs ={"placeholder " : "password..."}))
  
  class Meta:
    model = User
    fields = [
              'fname',
              'lname',
              'email',
              'password'
    	]