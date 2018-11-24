from django import forms
from .models import Dates,Appl



class DatesForm(forms.ModelForm):
	class Meta:
		model = Dates
		fields = [
			'applicant_number',
			'from_date',
			'to_date',

		]



class ApplForm(forms.ModelForm):
	class Meta:
		model = Appl
		fields = [
			'applicant_number',

		]