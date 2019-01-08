from django.urls import path, include
from . import views

app_name = 'malchance'

urlpatterns = [
	path('index', views.index, name="index"),
	path('', views.auth, name='auth'),
	path('Thingspeak/view/<int:channel>/<str:key>', views.thing, name='thing-view'),


	path('addmedecin', views.UserFormView.as_view(), name='addmedecin'),
	#showing all medecin in a table
	path('medecin/view', views.MedecinView.as_view(), name='medecin-view'),
	#malchance/detail of one médecin
	path('detail/medecin/<pk>', views.DetailMedecinView.as_view(), name='medecin-detail'),	
	# malchance/id
	path('medecin/<pk>', views.MedecinUpdate.as_view(), name="medecin-update"),	
	# malchance/id
	path('medecin/<pk>/delete', views.MedecinDelete.as_view(), name="medecin-delete"),


	#showing all appareilAuth in a table
	path('materielauth/view', views.MaterielAuthView.as_view(), name='materielauth-view'),
	#malchance/detail of one appareilAuth
	path('detail/materielauth/<pk>', views.DetailMaterielAuthView.as_view(), name='materielauth-detail'),
	# malchance/add appareilAuth
	path('materielauth/add', views.MaterielAuthCreate.as_view(), name="materielauth-add"),	
	# malchance/id appareilAuth
	path('materielauth/<pk>', views.MaterielAuthUpdate.as_view(), name="materielauth-update"),	
	# malchance/id appareilAuth
	path('materielauth/<pk>/delete', views.MaterielAuthDelete.as_view(), name="materielauth-delete"),





	#showing all appareilmesure in a table
	path('materielmesure/view', views.MaterielMesureView.as_view(), name='materielmesure-view'),
	#malchance/detail of one appareilmesure
	path('detail/materielmesure/<pk>', views.DetailMaterielMesureView.as_view(), name='materielmesure-detail'),
	# malchance/add appareilmesure
	path('materielmesure/add', views.MaterielMesureCreate.as_view(), name="materielmesure-add"),	
	# malchance/id appareilmesure
	path('materielmesure/<pk>', views.MaterielMesureUpdate.as_view(), name="materielmesure-update"),	
	# malchance/id appareilmesure
	path('materielmesure/<pk>/delete', views.MaterielMesureDelete.as_view(), name="materielmesure-delete"),



	#showing all patient in a table
	path('Patient/view', views.PatientView.as_view(), name='Patient-view'),
	#malchance/detail of one patient
	path('detail/Patient/<pk>', views.DetailPatientView.as_view(), name='Patient-detail'),
	# malchance/add patient
	path('Patient/add', views.PatientCreate.as_view(), name="Patient-add"),	
	# malchance/id patient
	path('Patient/<pk>', views.PatientUpdate.as_view(), name="Patient-update"),	
	# malchance/id patient
	path('Patient/<pk>/delete', views.PatientDelete.as_view(), name="Patient-delete"),
	





#showing all Dossier in a table
	path('Dossier/view', views.DossierView.as_view(), name='Dossier-view'),
	#malchance/detail of one Dossier
	path('detail/Dossier/<pk>', views.DetailDossierView.as_view(), name='Dossier-detail'),
	# malchance/add Dossier
	path('Dossier/add', views.DossierCreate.as_view(), name="Dossier-add"),	
	# malchance/id Dossier
	path('Dossier/<pk>', views.DossierUpdate.as_view(), name="Dossier-update"),	
	# malchance/id Dossier
	path('Dossier/<pk>/delete', views.DossierDelete.as_view(), name="Dossier-delete"),






#showing all Diagnostic in a table
	path('Diagnostic/view', views.DiagnosticView.as_view(), name='Diagnostic-view'),
	#malchance/detail of one Diagnostic
	path('detail/Diagnostic/<pk>', views.DetailDiagnosticView.as_view(), name='Diagnostic-detail'),
	# malchance/add Diagnostic
	path('Diagnostic/add', views.DiagnosticCreate.as_view(), name="Diagnostic-add"),	
	# malchance/id Diagnostic
	path('Diagnostic/<pk>', views.DiagnosticUpdate.as_view(), name="Diagnostic-update"),	
	# malchance/id Diagnostic
	path('Diagnostic/<pk>/delete', views.DiagnosticDelete.as_view(), name="Diagnostic-delete"),





#showing all Enregistrement in a table
	path('Enregistrement/view', views.EnregistrementView.as_view(), name='Enregistrement-view'),
	#malchance/detail of one Enregistrement
	path('detail/Enregistrement/<pk>', views.DetailEnregistrementView.as_view(), name='Enregistrement-detail'),
	# malchance/add Enregistrement
	path('Enregistrement/add', views.EnregistrementCreate.as_view(), name="Enregistrement-add"),	
	# malchance/id Enregistrement
	path('Enregistrement/<pk>', views.EnregistrementUpdate.as_view(), name="Enregistrement-update"),	
	# malchance/id Enregistrement
	path('Enregistrement/<pk>/delete', views.EnregistrementDelete.as_view(), name="Enregistrement-delete"),



#showing all PatientMesure in a table
	path('PatientMesure/view', views.PatientMesureView.as_view(), name='PatientMesure-view'),
	#malchance/detail of one PatientMesure
	path('detail/PatientMesure/<pk>', views.DetailPatientMesureView.as_view(), name='PatientMesure-detail'),
	# malchance/add PatientMesure
	path('PatientMesure/add', views.PatientMesureCreate.as_view(), name="PatientMesure-add"),	
	# malchance/id PatientMesure
	path('PatientMesure/<pk>', views.PatientMesureUpdate.as_view(), name="PatientMesure-update"),
	# malchance/id PatientMesureThing
	path('PatientMesureThing/<pk>', views.PatientMesureUpdateThing.as_view(), name="PatientMesureThing-update"),
	# malchance/id PatientMesure
	path('PatientMesure/<pk>/delete', views.PatientMesureDelete.as_view(), name="PatientMesure-delete"),

	

]
