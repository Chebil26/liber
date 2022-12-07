from django import forms
#rom django.db.models import fields


from .models import *


from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AnnonceForm(ModelForm):
	class Meta:
		model = Annonce
		fields = '__all__'
		exclude = ['publisher']
  
  
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
