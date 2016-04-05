from django import forms
from django.contrib.admin import widgets 
from django.db import models
from django.forms.widgets import TextInput, DateInput, DateTimeInput, TimeInput
import lavang.models
from .models import Family, Member
	
class MyTelephoneInput(TextInput):
    input_type = 'tel'

class MyDateInput(DateInput):
    input_type = 'date'

class MyDateTimeInput(DateTimeInput):
    input_type = 'datetime'

class MyTimeInput(TimeInput):
    input_type = 'time'
	
	
class LVForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(LVForm, self).__init__(*args, **kwargs)	
		for fieldname in self.fields:
			modelfield = self._meta.model._meta.get_field(fieldname)
			# Lookup key
			if isinstance(modelfield, models.ForeignKey):						
				self.fields[fieldname].widget.attrs.update({'class': 'form-control input-sm'})							
			if isinstance(modelfield, models.CharField):			
				self.fields[fieldname].widget.attrs.update({'class': 'form-control input-sm'})	
			# date field
			if isinstance(modelfield, models.DateField):
				self.fields[fieldname].widget.attrs.update({'class': 'form-control input-sm datepicker', 'readonly': 'readonly'})	
				
			# email field
			if isinstance(modelfield, models.EmailField):
				self.fields['mem_sEmailAddress'].widget.attrs.update({'type': 'email', 'pattern': '[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}'})


class SearchMemberForm(forms.Form):
	Family_ID = forms.IntegerField(required=False, label='Family #', widget=forms.NumberInput(attrs={'class': 'form-control input-sm'}))
	Last_Name = forms.CharField(max_length=20,required=False, label='Last', widget=forms.TextInput(attrs={'class': 'form-control input-sm'}))
	First_Name = forms.CharField(max_length=20,required=False, label='First', widget=forms.TextInput(attrs={'class': 'form-control input-sm'}))
	Street = forms.CharField(max_length=80,required=False, label='Street', widget=forms.TextInput(attrs={'class': 'form-control input-sm'}))
	City = forms.CharField(max_length=32,required=False, label='City', widget=forms.TextInput(attrs={'class': 'form-control input-sm'}))
	Home_Phone= forms.CharField(max_length=12,required=False, label='Home Phone', widget=forms.TextInput(attrs={'class': 'form-control input-sm'}))
	Mobile= forms.CharField(max_length=12,required=False, label='Mobile Phone', widget=forms.TextInput(attrs={'class': 'form-control input-sm'}))	
		
class FamilyForm(LVForm):
	def __init__(self, *args, **kwargs):
		super(FamilyForm, self).__init__(*args, **kwargs)	
	class Meta:
		fields = ('fam_iChurchID', 'fam_iFamilyID', 'fam_sStreet', 'fam_sCity', 'fam_sState', 'fam_sPostalCode', 'fam_sPhone', 'fam_sFamilyEligibility', 'fam_oPortrait', )
        #This is the association between the model and the model form
		model = Family

class MemberDetailForm(LVForm):
	def __init__(self, *args, **kwargs):
		super(MemberDetailForm, self).__init__(*args, **kwargs)
		self.fields['mem_iFamilyID'].widget.attrs.update({'readonly': 'readonly'})
		# Mobile Phone
		self.fields['mem_sMobile'].widget = MyTelephoneInput(attrs={'class': 'form-control input-sm','pattern':'\(?(\d{3})\)?[ -.](\d{3})[ -.](\d{4})'})

	class Meta:
		fields = ('mem_iMemberID','mem_iFamilyID', 'mem_sChristianName', 'mem_sFirstName', 'mem_sLastName', 'mem_sMiddleName', 'mem_sMemberRole', 'mem_dtDayOfBirth', 'mem_sCityOfBirth', 'mem_sCountryOfBirth', 'mem_sGender', 'mem_sNationality', 'mem_sMartialStatusID', 'mem_sMobile','mem_sEmailAddress', 'mem_dtExit', 'mem_sMemo', 'mem_oPortrait')
        #This is the association between the model and the model form
		model = Member	
		#exclude  = ('mem_oPortrait',)
		
	def clean(self):
		cleaned_data = super(MemberDetailForm, self).clean()	
		
class MemberGridForm(LVForm):

	def __init__(self, *args, **kwargs):
		super(MemberGridForm, self).__init__(*args, **kwargs)

	class Meta:
		fields = ('mem_iMemberID','mem_iFamilyID', 'mem_sChristianName', 'mem_sFirstName', 'mem_sLastName', 'mem_sMiddleName', 'mem_sMemberRole', 'mem_dtDayOfBirth', 'mem_sCityOfBirth', 'mem_sCountryOfBirth', 'mem_sGender', 'mem_sNationality', 'mem_sMartialStatusID', 'mem_sMobile')
        #This is the association between the model and the model form
		model = Member	
		#exclude  = ('mem_oPortrait',)		