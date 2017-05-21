from django.db import models
from django.utils import timezone

class Person(models.Model):
	blood_group_choices= (
		('A+','A+'), ('B+','B+'), ('AB+','AB+'), ('O+','O+'), ('A-','A-'), ('B-','B-'), ('AB-','AB-'), ('O-','O-')
		)
	blood_group =models.CharField(max_length=3, choices=blood_group_choices)
	#blood_group = models.ChoiceField('A+','B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-')
	name = models.CharField(max_length=60)
	contact = models.DecimalField(max_digits=10,decimal_places=0)
	address = models.CharField(max_length=150)
	post_date = models.DateTimeField()
	
	class Meta:
		db_table ="Person"

	def __str__(self):
		return self.name		
	