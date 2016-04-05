from django import forms

class SearchMemberForm(forms.Form):
	Family_ID = forms.IntegerField(required=False, label='Family #')
	Last_Name = forms.CharField(max_length=20,required=False, label='Last')
	First_Name = forms.CharField(max_length=20,required=False, label='First')
	Street = forms.CharField(max_length=80,required=False, label='Street')
	City = forms.CharField(max_length=32,required=False, label='City')
	Home_Phone= forms.CharField(max_length=12,required=False, label='Home Phone')
	Mobile= forms.CharField(max_length=12,required=False, label='Mobile Phone')	