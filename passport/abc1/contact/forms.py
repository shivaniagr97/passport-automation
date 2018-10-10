from django import forms


class contactForms(forms.Form):
	name = forms.CharField(required = False,max_length=100,help_text = 'max 100 chars allowed')
	email = forms.EmailField(required = True)
	comment = forms.CharField(required = True,widget=forms.Textarea)