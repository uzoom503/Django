from django import forms
from .models import Family

class FamilyForm(forms.ModelForm):

	class Meta:
		fields = ('fam_iChurchID', 'fam_iFamilyID', 'fam_sStreet', 'fam_sCity', 'fam_sState', 'fam_sPostalCode', 'fam_sPhone', 'fam_sMobile', 'fam_sFamilyEligibility', 'fam_oPortrait', )
        #This is the association between the model and the model form
		model = Family