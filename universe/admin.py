from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class PersonaResource(resources.ModelResource):
    class Meta:
        model=Persona

class PersonaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['id_user']
    list_display=('id_user','name','lastname')
    resource_class=PersonaResource
    

admin.site.register(Persona, PersonaAdmin)
admin.site.register(UniverseManageResponsable)
admin.site.register(UniverseMacroproces)
admin.site.register(UniverseProces)