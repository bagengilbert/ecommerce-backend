from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import customUser

#custom for user registration,extending the built in usercreationform 

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=customUser
        fields=['username', 'email' , 'phone_Number', 'address']
