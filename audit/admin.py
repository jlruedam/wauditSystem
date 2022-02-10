from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class AuditResource(resources.ModelResource):
    class Meta:
        model=Audit

class AuditAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields=['idAudit']
    list_display=('idAudit','auditor')
    resource_class=Audit
   

admin.site.register(Audit, AuditAdmin)

