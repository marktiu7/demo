from django.forms import ModelForm
from django import forms
from blog.models import *

#blog
'''
class UserForm(forms.Form):
     username=forms.CharField()
     password=forms.CharField( widget= forms.PasswordInput )
'''


class UserForm(ModelForm):
     class Meta:
         model=User
         fields =('username','password','email')
         labels = {
            'username': 'yonghuming',
            
             }
         widgets = {
             'password':forms.PasswordInput,
             
         }
         
         error_messages = {
            'email': {
                'invalid': "This writer's name is too long.",
            },
        }
         