from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *


# Create your views here.
#@login_reqired
# page d'index ce que l'on voit en premier aprés la connexion
def index(request):
	template = "code/index.html"
	request.session['userid'] = request.user.id
	return render(request,template)



def thing(request, channel, key):
	src = "global/Thingspeak.html"
	#value = 75470
	context = {
		'idthing' : channel,
		'key' : key
	}
	return render(request, src, context)

# gérer l'authentification
def auth(request):
	if request.user.is_authenticated:
		return redirect("malchance:index")		
	else:
		form = Auth()
		context ={
			'form' : form
		}
		return render(request, 'registration/login.html',context)





# gére les médecins 
class MedecinView(generic.ListView):
	template_name = "code/medecin-view.html"
	context_object_name = 'Allmedecin'
	def get_queryset(self):
		return Medecin.objects.all()


class DetailMedecinView(generic.DetailView):
	model = Medecin
	template_name = "code/medecin-detail.html"



class MedecinUpdate(UpdateView):
	model = Medecin
	template_name = 'code/object-add.html'
	fields = ['username', 'first_name', 'last_name', 'email', 'Specialization']


class MedecinDelete(DeleteView):
	model = Medecin
	template_name = "code/delete.html"
	success_url = reverse_lazy('malchance:medecin-view')

class UserFormView(View):
	form_class = MedecinForm
	template_name = 'code/object-add.html'

	#display a blank form
	def get(self,request):
		context = {'form': self.form_class(None)}
		return render(request, self.template_name, context)

	#process from data 
	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit = False)
			# cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			Specialization = form.cleaned_data['Specialization']
			user.set_password(password)
			user.save()
			return redirect('malchance:medecin-detail', pk=user.pk)
		else: 
			context = {'form': self.form_class(request.POST)}
			return render(request, self.template_name, context)






# for matériel d'authentification
class MaterielAuthView(generic.ListView):
	template_name = "code/materielauth-view.html"
	context_object_name = 'AllMaterielAuth'
	def get_queryset(self):
		return MaterielAuth.objects.all()


class DetailMaterielAuthView(generic.DetailView):
	model = MaterielAuth
	template_name = "code/materielauth-detail.html"


class MaterielAuthCreate(CreateView):
	model = MaterielAuth
	template_name = "code/object-add.html"
	fields = ['CodeIdentification']


class MaterielAuthUpdate(UpdateView):
	model = MaterielAuth
	template_name = "code/object-add.html"
	fields = ['CodeIdentification', 'etat']


class MaterielAuthDelete(DeleteView):
	model = MaterielAuth
	template_name = "code/delete.html"
	success_url = reverse_lazy('malchance:materielauth-view')







# for matériel de mesure
class MaterielMesureView(generic.ListView):
	template_name = "code/materielmesure-view.html"
	context_object_name = 'Allmaterielmesure'
	def get_queryset(self):
		return MaterielMesure.objects.all()


class DetailMaterielMesureView(generic.DetailView):
	model = MaterielMesure
	template_name = "code/materielmesure-detail.html"


class MaterielMesureCreate(CreateView):
	model = MaterielMesure
	template_name = "code/object-add.html"
	fields = ['IdMaterielMesure']


class MaterielMesureUpdate(UpdateView):
	model = MaterielMesure
	template_name = "code/object-add.html"
	fields = ['IdMaterielMesure', 'etat']


class MaterielMesureDelete(DeleteView):
	model = MaterielMesure
	template_name = "code/delete.html"
	success_url = reverse_lazy('malchance:materielmesure-view')






# for Patient
class PatientView(generic.ListView):
	template_name = "code/Patient-view.html"
	context_object_name = 'AllPatient'
	def get_queryset(self):
		return Patient.objects.all()


class DetailPatientView(generic.DetailView):
	model = Patient
	template_name = "code/Patient-detail.html"


class PatientCreate(CreateView):
	model = Patient
	template_name = "code/object-add.html"
	fields = ['NomPatient', 'PrenomPatient', 'DateNaissPatient', 'Address', 'Sexe']


class PatientUpdate(UpdateView):
	model = Patient
	template_name = "code/object-add.html"
	fields = ['NomPatient', 'PrenomPatient', 'DateNaissPatient', 'Address', 'Sexe']


class PatientDelete(DeleteView):
	model = Patient
	template_name = "code/delete.html"
	success_url = reverse_lazy('malchance:Patient-view')
















# for Dossier
class DossierView(generic.ListView):
	template_name = "code/dossier-view.html"
	context_object_name = 'AllDossier'
	def get_queryset(self):
		return Dossier.objects.filter(IdMedecin=self.request.session.get('userid')).values()


class DetailDossierView(generic.DetailView):
	model = Dossier
	template_name = "code/dossier-detail.html"

	#def Dossier_detail_view(request, patientid):
	#   try:
	#        enregistrement = Enregistrement.objects.get(IdPatient=patientid)
	#   except enregistrement.DoesNotExist:
	#       raise Http404('Enregistrement does not exist')	    
	#   return render(request, 'code/enregistrement-view.html', context={'book': book})


class DossierCreate(CreateView):
	model = Dossier
	template_name = "code/object-add.html"
	fields = ['IdDossier', 'IdPatient']
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.IdMedecin = Medecin.objects.get(id=self.request.session.get('userid'))
		obj.save()
		return redirect('malchance:Dossier-detail', pk=obj.pk)


class DossierUpdate(UpdateView):
	model = Dossier
	template_name = "code/object-add.html"
	fields = ['IdDossier', 'IdPatient', 'IdMedecin']


class DossierDelete(DeleteView):
	model = Dossier
	template_name = "code/delete.html"
	success_url = reverse_lazy('malchance:Dossier-view')








# for Diagnostic
class DiagnosticView(generic.ListView):
	template_name = "code/diagnostic-view.html"
	context_object_name = 'AllDiagnostic'
	def get_queryset(self):
		return Diagnostic.objects.all()
		#return Diagnostic.objects.filter(IdDossier=Dossier.objects.filter(IdMedecin=self.request.session.get('userid'))).values()


class DetailDiagnosticView(generic.DetailView):
	model = Diagnostic
	template_name = "code/diagnostic-detail.html"


class DiagnosticCreate(CreateView):
	model = Diagnostic
	template_name = "code/object-add.html"
	fields = ['IdDossier', 'Titre', 'contenu', 'recommendation']


class DiagnosticUpdate(UpdateView):
	model = Diagnostic
	template_name = "code/object-add.html"
	fields = ['IdDossier', 'Titre', 'contenu', 'recommendation']


class DiagnosticDelete(DeleteView):
	model = Diagnostic
	template_name = "code/delete.html"
	success_url = reverse_lazy('malchance:Diagnostic-view')















# for Enregistrement
class EnregistrementView(generic.ListView):
	template_name = "code/enregistrement-view.html"
	context_object_name = 'AllEnregistrement'
	def get_queryset(self):
		#Idpat = Dossier.objects.filter(IdMedecin=self.request.session.get('userid')).values()
		#self.IdDossier = get_object_or_404(Dossier, IdDossier=self.)
		#Idpat = Dossier.objects.filter(id=self.kwargs['doss']).values("IdPatient")
		#return Enregistrement.objects.filter(IdPatient=Idpat).values()
		return Enregistrement.objects.all()


class DetailEnregistrementView(generic.DetailView):
	model = Enregistrement
	template_name = "code/enregistrement-detail.html"


class EnregistrementCreate(CreateView):
	model = Enregistrement
	template_name = "code/object-add.html"
	#Idpat = Dossier.objects.get(IdMedecin=self.request.session.get('userid'))
	#Enregistrement.IdPatient = Idpat.IdPatient
	fields = ['Titre', 'valeur', 'Date']
	def form_valid(self, form):
		obj = form.save(commit=False)
		Idpat = Dossier.objects.get(IdMedecin=self.request.session.get('userid'))
		obj.IdPatient = Idpat.IdPatient
		obj.save()
		return redirect('malchance:Enregistrement-detail', pk=obj.pk)



class EnregistrementUpdate(UpdateView):
	model = Enregistrement
	template_name = "code/object-add.html"
	fields = ['IdPatient', 'Titre', 'valeur', 'Date']


class EnregistrementDelete(DeleteView):
	model = Enregistrement
	template_name = "code/delete.html"
	success_url = reverse_lazy('malchance:Enregistrement-view')















# for PatientMesure
class PatientMesureView(generic.ListView):
	template_name = "code/PatientMesure-view.html"
	context_object_name = 'AllPatientMesure'
	def get_queryset(self):
		return PatientMesure.objects.all()

class DetailPatientMesureView(generic.DetailView):
	model = PatientMesure
	template_name = "code/PatientMesure-detail.html"


#class MesureCreate(object):
#	form_class = PatientMesureForm
#	template_name = "code/object-add.html"
#
#	def get(self, request):
#		context = {'form' : self.form_class(None)}
#		return render(request,self.template_name, context)
#	def post(self,request):
#		form = self.form_class(request.POST)
#		if form.is_valid():
#			mesure = form.save(commit = False)




class PatientMesureCreate(CreateView):
	model = PatientMesure
	template_name = "code/ThingAdd.html"
	fields = ['IdAttach','IdPatient', 'IdMaterielMesure','DateBegin']
	
class PatientMesureUpdate(UpdateView):
	model = PatientMesure
	template_name = "code/object-add.html"
	fields = ['IdPatient', 'IdMaterielMesure','IdChannel','PublicKey','DateBegin','DateEnd']

class PatientMesureUpdateThing(UpdateView):
	model = PatientMesure
	template_name = "code/ThingChannel.html"
	fields = ['IdChannel','PublicKey']

class PatientMesureDelete(DeleteView):
	model = PatientMesure
	template_name = "code/delete.html"
	success_url = reverse_lazy('malchance:PatientMesure-view')