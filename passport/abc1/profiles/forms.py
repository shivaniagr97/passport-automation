from django import forms
from .models import Details,Documents

class DetailsForm(forms.ModelForm):
	class Meta:
		model=Details
		fields=[
			'name',
			'house_no',
			'colony_or_location',
			'city',
			'district',
			'state',
			'pin_code',
			'contact_number',
			'emergency_contact_number',
			'email_id',
			'gender',
			'marital_status',
			'date_of_birth',
			'birth_place',
			'employement_status',
			'pan',
			'voter_id',
			'aadhar_number',
			'father_name',
			'mother_name',
			'guardian_name',
			'spouse_name',
			'educational_qualification',
		]
	def __init__(self,*args,**kwargs):
		super(DetailsForm,self).__init__(*args,**kwargs)
		self.fields['pan'].required=False
		self.fields['voter_id'].required=False
		self.fields['guardian_name'].required=False
		self.fields['spouse_name'].required=False

class DocumentsForm(forms.ModelForm):
	class Meta:
		model = Documents
		fields = [
			'aadhar_card',
			'address_proof',
			'birth_certificate_or_matric_marksheet',
			'photo'

		]