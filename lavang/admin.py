from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.conf.urls import patterns  
from .models import Church, Family, Member

class ChurchAdmin(admin.ModelAdmin):
	list_display = ['chu_sName', 'chu_sStreet', 'chu_sCity', 'chu_sState', 'chu_sPostalCode', 'chu_sPhone','chu_sEmailAddress','chu_sMissionStatement', 'chu_sMemo', 'chu_sURLWebsite']
admin.site.register(Church, ChurchAdmin)

class FamilyAdmin(admin.ModelAdmin):
	list_display = ['fam_iChurchID', 'fam_iFamilyID', 'fam_sStreet', 'fam_sCity', 'fam_sState', 'fam_sPostalCode', 'Phone',
	 'fam_dtEntry', 'fam_dtExit']
	list_filter = ['fam_sCity', 'fam_sState','fam_sPostalCode']
	search_fields = ('fam_iFamilyID',)
	list_editable = []
admin.site.register(Family, FamilyAdmin)


