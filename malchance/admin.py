from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Medecin)
admin.site.register(MaterielMesure)
admin.site.register(MaterielAuth)
admin.site.register(MedecinAuth)