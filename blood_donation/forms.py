from django import forms
from .models import Person

# Create the form class.

class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ['blood_group', 'name', 'contact', 'address']


# Creating a form to add an Person.
form = PersonForm()		

# Creating a form to change an existing Person.
