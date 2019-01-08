from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# Create your models here.

class Medecin(User):
	Specialization = models.CharField(max_length=50, default="Generaliste")

	def get_absolute_url(self):
		return reverse('malchance:medecin-detail', kwargs={'pk': self.pk})

class MaterielAuth(models.Model):
	CodeIdentification = models.CharField(max_length=60, default='null')
	etats = (
		('A','Activer'),
		('D','Desactiver'),
		)
	etat = models.CharField(max_length=1, choices=etats, default='D')
	
	def get_absolute_url(self):
		return reverse('malchance:materielauth-detail', kwargs={'pk': self.pk})
		

class MedecinAuth(models.Model):
	IdMedecin = models.ForeignKey(Medecin, on_delete=models.DO_NOTHING)
	CodeIdentification = models.ForeignKey(MaterielAuth, on_delete=models.DO_NOTHING)
	DateBegin = models.DateField(("Date"), default=date.today)
	DateEnd = models.DateField(blank=True, null=True)

class MaterielMesure(models.Model):
	IdMaterielMesure = models.CharField(max_length=250, default='null')
	etats = (
		('A','Activer'),
		('D','Desactiver'),
		)
	etat = models.CharField(max_length=1, choices=etats, default='D')

	def get_absolute_url(self):
		return reverse('malchance:materielmesure-detail', kwargs={'pk': self.pk})

class Patient(models.Model):
	NomPatient = models.CharField(max_length=250)
	PrenomPatient = models.CharField(max_length=250)
	DateNaissPatient = models.DateField()
	Address = models.CharField(max_length=250)
	sex = (
    	('F', 'Femme'),
    	('M', 'Homme'),
	)
	Sexe = models.CharField(max_length=1, choices=sex)
	def get_absolute_url(self):
		return reverse('malchance:Patient-detail', kwargs={'pk': self.pk})


class Dossier(models.Model):
	IdDossier = models.CharField(max_length=25, default="null")
	IdPatient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
	IdMedecin = models.ForeignKey(Medecin, on_delete=models.DO_NOTHING)
	def get_absolute_url(self):
		return reverse('malchance:Dossier-detail', kwargs={'pk': self.pk})


class Diagnostic(models.Model):
	IdDossier = models.ForeignKey(Dossier, on_delete=models.DO_NOTHING)
	Titre = models.CharField(max_length=250)
	contenu = models.TextField()
	recommendation = models.TextField(blank=True)
	def get_absolute_url(self):
		return reverse('malchance:Diagnostic-detail', kwargs={'pk': self.pk})


class Enregistrement(models.Model):
	IdPatient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
	Titre = models.CharField(max_length=250, default='null')
	valeur = models.CharField(max_length=25)
	Date = models.DateField()
	def get_absolute_url(self):
		return reverse('malchance:Enregistrement-detail', kwargs={'pk': self.pk})


class PatientMesure(models.Model):
	IdAttach = models.CharField(max_length=255, default="null")
	IdPatient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
	IdMaterielMesure = models.ForeignKey(MaterielMesure, on_delete=models.DO_NOTHING)
	IdChannel = models.CharField(max_length=30, default="null")
	PublicKey = models.CharField(max_length=30, default="null")
	DateBegin = models.DateField(("Date"), default=date.today)
	DateEnd = models.DateField(blank=True, null=True)
	def get_absolute_url(self):
		return reverse('malchance:PatientMesure-detail', kwargs={'pk': self.pk})


