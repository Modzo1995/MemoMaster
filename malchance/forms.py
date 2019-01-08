from django.contrib.auth.models import User
from django import forms
from .models import *

class MedecinForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Medecin
		fields = ['username', 'password', 'first_name', 'last_name', 'email', 'Specialization']


class Auth(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput({
										'class':'form-control',
										'placeholder':'nom d\'utilisateur'
									}))
	password = forms.CharField(widget=forms.PasswordInput({
									'class' : 'form-control',
									'placeholder' : 'mot de passe'
								}))
	class Meta:
		model = User
		fields = ['username', 'password']


class PatientMesureForm(forms.ModelForm):
	DateBegin = forms.DateTimeField()
	class Meta:
		model = PatientMesure
		fields = ['IdPatient', 'IdMaterielMesure','DateBegin']