from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = '__all__'

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class RiderForm(forms.ModelForm):
	class Meta:
		model = Rider
		fields = '__all__'

class StoreForm(forms.ModelForm):
	class Meta:
		model = Store
		fields = '__all__'